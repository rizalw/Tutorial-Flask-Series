from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/coba")
def coba():
    return render_template("next.html")

if __name__ == "__main__":
    app.run(debug=True)