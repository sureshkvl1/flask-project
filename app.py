from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_whale():
    #return render_template("whale_hello.html")
    return '<html><body bgcolor="#E6E00F"><h1>hello world</h1></body></html>'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
