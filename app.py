from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', message='Hello, World!')

@app.route("/test")
def placeholder():
    return render_template('index.html', message='I am 7 years old')

if __name__ == '__main__':
    app.run(debug=True)

# use 'python app.py' then go to http://127.0.0.1:5000/ to preview