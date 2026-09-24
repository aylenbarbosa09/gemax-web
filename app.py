from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/hombre")
def hombre():
    return render_template("hombre.html")

@app.route("/mujer")
def mujer():
    return render_template("mujer.html")

@app.route("/zapas")
def zapas():
    return render_template("zapas.html")

if __name__ == "__main__":
    app.run(debug=True)