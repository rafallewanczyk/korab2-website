from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<a href='test'><h1>hello-world</h1></a>"

@app.route("/test")
def test_view():
    return "<h1>this is test view</h1>"