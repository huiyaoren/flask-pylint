# flask-pylint

一个基于 pre-commit 的简易 flask pylint 扩展

## 安装

```bash
pip install git+https://github.com/huiyaoren/flask-pylint
```

## 使用

使用方式同常见 flask 扩展一致

```python
from flask_pylint import Pylint

pylint = Pylint(app)
```

## 配置

`PYLINT_DISABLE`  disable pylint check if value is `True`
