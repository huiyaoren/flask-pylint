# flask-pylint

一个基于 pre-commit 的简易 flask pylint 扩展。

## 安装

```bash
pip install git+https://github.com/huiyaoren/flask-pylint
```

## 使用

使用方式同常见 flask 扩展一致。

```python
from flask_pylint import Pylint

pylint = Pylint(app)
```

在项目根目录创建 `.pre-commit-config.yaml`，例：

```yaml
repos:

- repo: https://github.com/pre-commit/mirrors-pylint
  rev: v2.7.4
  hooks:
  - id: pylint
    args:
    - --score=y
    - --disable=C0103,C0114,C0115,C0116,E0401,R0903,R1722,W0105,W0108,W0401,W0614
    - --ignore=docker,venv
    - --fail-under=9.3
    - --max-line-length=120
```

完成后启动 flask 时将进行代码风格检查：

```bash
pre-commit installed at .git\hooks\pre-commit
pylint...................................................................Passed
```

## 配置

`PYLINT_DISABLE`: 当值为 `True` 时关闭 pylint 代码检查。
