from flask import Flask, request, render_template

app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", data="POST data is displayed here.")
    
    if request.method == "POST":
        return render_template("index.html", data=request.form.get("data"))


app.run(host="0.0.0.0", port=8080)