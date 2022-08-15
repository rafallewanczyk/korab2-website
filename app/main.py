from flask import Flask, current_app

app = Flask(__name__, static_folder='web/static', static_url_path='')


@app.route("/")
def home_view():
    return current_app.send_static_file('index.html')
