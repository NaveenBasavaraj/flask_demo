# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/aboutus")
def f2():
    return render_template("index.html")

@app.route("/city")
def f3():
    myName = "naveen"
    return render_template("index.html", tName=myName)

if __name__ == "__main__":
    app.run(debug=True)