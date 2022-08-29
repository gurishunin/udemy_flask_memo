from flask import Flask
from flask import render_template,g,redirect,request
import sqlite3
DATABASE="flaskmemo.db"

app = Flask(__name__)

@app.route("/")
def top():
    memo_list = get_db().execute("select id,title,body from memo").fetchall()
    return render_template('index.html',memo_list=memo_list)

@app.route("/regist",methods=['GET','POST'])
def regist():
    if request.method =='POST':
        #画面からの登録情報の取得
        title = request.form.get('title')
        body = request.form.get('body')
        db = get_db()
        db.execute("insert into memo (title,body) values(?,?)",[title,body])
        db.commit()
        return redirect('/')
    
    return render_template('regist.html')

if __name__ == "__main__":
    app.run()

#database
def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv
def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db