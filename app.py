from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# use 'flask app run' then go to http://127.0.0.1:5000/ to preview