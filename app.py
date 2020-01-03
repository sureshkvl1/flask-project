from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_whale():
    return '<html><body bgcolor="#E6E000"><h1>hello </h1></body></html>'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
