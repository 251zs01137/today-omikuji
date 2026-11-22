from flask import Flask, render_template
import random

app = Flask(__name__)

FORTUNES = [
    {"name": "大吉", "message": "最高の一日になりそう！新しいことに挑戦してみよう。", "item": "青いペン", "color": "#e85d75"},
    {"name": "中吉", "message": "落ち着いて行動すれば、うれしい発見がありそう。", "item": "お気に入りの飲み物", "color": "#e59b38"},
    {"name": "小吉", "message": "小さな幸せを見つけられる日。周りに目を向けてみて。", "item": "ハンカチ", "color": "#4e9b83"},
    {"name": "吉", "message": "いつも通りがいちばん。自分のペースで進もう。", "item": "腕時計", "color": "#668bd1"},
    {"name": "末吉", "message": "これから運気が上がっていく予感。焦らずゆっくり。", "item": "チョコレート", "color": "#9671b5"},
    {"name": "凶", "message": "今日は無理をせず、丁寧に過ごすのがよさそう。", "item": "温かいお茶", "color": "#777777"},
]

@app.route("/")
def index():
    return render_template("index.html", fortune=None)

@app.route("/draw")
def draw():
    fortune = random.choice(FORTUNES)
    return render_template("index.html", fortune=fortune)

if __name__ == "__main__":
    app.run(debug=True)
