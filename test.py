from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Denis!'


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')