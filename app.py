from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list = [
    {'title':"test01",'body':"ぐり主任です。"},
    {'title':"test02",'body':"ぐらです。"},
    #{'title':"test03",'body':"test03"}
]

@app.route("/")
def top():
    return render_template('index.html',memo_list=memo_list)

if __name__ == "__main__":
    app.run()
