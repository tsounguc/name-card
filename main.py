from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home(name=None):
    return render_template('index.hmtl', name=name)
