import os
from flask import Flask, request
import json

server_ip = "localhost"
server_port = 5000
top_n = 3
reset_token = "PLEASE-CHANGE-ME"
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# 保存玩家传来的分数
@app.route("/save")
def get_score_from_player():
    player_name = request.args.get("name") or "Player"
    score = request.args.get("score") or 0
    save_score(player_name, score)

    s = "{} {}".format(player_name, score)
    return s

def save_score(player_name, score):
    try:
        with open("scoreboard.json", "r") as f:
            scoreboard = json.load(f)
    except:
        scoreboard = []
    
    obj = {
        'name': "".join([i if ord(i) < 128 else "" for i in player_name]),
        'score': int(score)
    }
    scoreboard.append(obj)
    scoreboard = [dict(i) for i in set([tuple(o.items()) for o in scoreboard])]
    scoreboard = sorted(scoreboard, key =lambda a:(a.__getitem__('score'),a.__getitem__('name')), reverse=True)
    scoreboard = scoreboard[:top_n]

    with open("scoreboard.json", "w") as f:
        json.dump(scoreboard, f)

# 玩家获取排行榜
@app.route("/score")
def player_get_scoreboard():
    try:
        with open("scoreboard.json", "r") as f:
            scoreboard = json.load(f)
    except:
        scoreboard = []

    s = str()
    for item in scoreboard:
        s += '{},{}\n'.format(item['name'], item['score'])
    return s

@app.route("/reset")
def clear_scoreboard():
    token = request.args.get("token")
    if token == reset_token:
        with open("scoreboard.json", "w") as f:
            f.truncate()
            return "Success"
    else:
        return "Failed"

if __name__ == '__main__':
    app.run(host=server_ip, port=server_port, debug=True)