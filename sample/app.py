from flask import Flask
from flask_pylint import Pylint

app = Flask(__name__)

Pylint(app)

if __name__ == '__main__':
    app.run(debug=True)
