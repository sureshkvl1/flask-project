from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_whale():
    #return render_template("whale_hello.html")
    return '<html><body bgcolor="#E6E000"><h1>hello Suresh Kumar1</h1></body></html>'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
