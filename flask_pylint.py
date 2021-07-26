import os
import subprocess


class Pylint:

    def __init__(self, app=None):
        self._disable = False
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        # 避免在 flask debug 模式下重复执行
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
            return self

        if 'PYLINT_DISABLE' in app.config:
            self._disable = app.config.get('PYLINT_DISABLE')
        else:
            self._disable = not app.config.get('DEBUG', True)

        if self._disable:
            return self

        self._prepare_hook()
        self._check_code()

        return self

    @staticmethod
    def _prepare_hook():
        subprocess.call(['pre-commit', 'install'])

    @staticmethod
    def _check_code():
        # 预检查代码风格
        _, output = subprocess.getstatusoutput('pre-commit run --all-files')
        # 输出最差评分代码信息
        output_lines = output.split('\n')
        for line in output_lines[0:3]:
            print(line)

        worst_score_info = []
        current_info = []
        worst_score = 10
        for line in output_lines[3:]:
            current_info.append(line)

            if line.startswith('Your code has been rated at'):
                score = float(line.split()[6].split('/')[0])
                if score < worst_score:
                    worst_score = score
                    worst_score_info = tuple(current_info)
                current_info = []

        for line in worst_score_info:
            print(line)
        # 通过检查或无法获取最差分数的场合 直接输出所有信息
        if not worst_score_info:
            for line in output_lines[3:]:
                print(line)
