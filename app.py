from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/imaginary-inspirations")
def imaginary_inspirations():
    return render_template("imaginary_inspirations.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)


