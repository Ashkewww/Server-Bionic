from http.client import HTTPResponse
from flask import Flask, render_template, request, jsonify
from apis.define import define
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/define', methods=['POST'])
async def define_word():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        word = data['word']
        print(word)
        va = await define(word)
        return va
    else:
        return {"error": "Invalid Request"}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if request.is_json:
            js = request.get_json()
            print(js['Hell'])
        return render_template('login.html')
    else:
        return


if __name__ == '__main__':
    app.run(debug=True)
