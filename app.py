from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/guri")
def hello_guri():
    return "<p>Hello, ぐり主任!</p>"

@app.route("/gura")
def hello_gura():
    return "<p>Hello, ぐらさん!</p>"


if __name__ == "__main__":
    app.run()
