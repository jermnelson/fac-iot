from flask import Flask, render_template, abort

app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def index():
    return render_template("index.html")
    
