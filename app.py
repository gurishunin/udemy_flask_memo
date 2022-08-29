from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"<p>Hello, { name }!</p>"

if __name__ == "__main__":
    app.run()
