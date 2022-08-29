# 設計を理解しながらWebアプリを開発【はじめてのWeb開発】【Flask】

こちらはぐり主任がUdemyで公開している「設計を理解しながらWebアプリを開発【はじめてのWeb開発】【Flask】」のリポジトリです。

詳細は[Udemyのコース](https://www.udemy.com/course/flask_memo/?referralCode=BD7134D728DFC04E8273)をご覧ください。

[GitHubリポジトリはこちら](https://github.com/gurishunin/udemy_flask_memo)

## コマンド一覧
### 仮想環境の構築
#### macOS/Linux
```
mkdir myproject
cd myproject
python3 -m venv venv
```
#### Windows
```
mkdir myproject
cd myproject
py -3 -m venv venv
```
### 仮想環境の有効化
#### macOS/Linux
```
. venv/bin/activate
```
#### Windows
```
venv\Scripts\activate
```
### Flaskのインストール
```
pip install Flask
```
### プログラムの実行コマンド
#### Mac(Bash)
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
#### Windows(CMD)※コマンドプロンプト
```
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
#### Windows(PowerShell)
```
$env:FLASK_APP = “app“
$env: FLASK_ENV = “development“
flask run
```

### Flask-loginのインストール
```
pip install flask-login
```


## ソースコード対応表
| セクション名 | レクチャー名                                 | ブランチ名     | 
| ------------|-------------------------------------------- | ------------- | 
| 【基礎】Webサーバを構築しよう！ | HelloWorld_プログラム作成 | 01_01_hello |
| 【基礎】Webサーバを構築しよう！ | ルーティング_実装 | 01_02_routing |
| 【基礎】Webサーバを構築しよう！ | ルーティング変数_実装 | 01_03_routing_2|
| 【基礎】Webサーバを構築しよう！ | 画面(HTML)テンプレート_実装 | 01_04_templates|
| 【基礎】Webサーバを構築しよう！ | 画面内条件分岐_実装 | 01_05_templates_2|
| 【開発】top画面を作ろう！ | - | 02_top|
| 【開発】DBの基礎を学ぼう！ | - | 03_top_db|
| 【開発】新規登録画面／機能を作ろう！ | - | 04_regist|
| 【開発】編集画面／機能を作ろう！ | - | 05_edit|
| 【開発】削除画面／機能を作ろう！ | - | 06_delete|
| 【開発】ログイン画面／機能を作ろう！①（DBなしで仕組みを作る） | - | 07_login|
| 【開発】ログイン画面／機能を作ろう！②（DB利用） | 完成版 | main|

## 各種リンク
[python公式ページ](https://www.python.org/downloads/)

[Flaskの公式ページ（英語）](https://flask.palletsprojects.com/en/latest/)

[Flaskの公式ページ（日本語）](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/)

[VScode](https://code.visualstudio.com/download)

[SQLite](https://www.sqlite.org/download.html)

[Flask-loginの公式ページ](https://flask-login.readthedocs.io/en/latest/)

