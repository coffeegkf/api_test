from flask import Flask, jsonify, abort
from flask import Request
import random

app = Flask(__name__)

@app.route("/api/user/reg/", methods=["POST"])
def reg():
    if not Request.json or not 'name' in Request.json or not 'password' in Request.json:
        abort(404)
    res = [
        {
            "code": "100000",
            "msg": "success",
            "data": {
                "name": "liliu",
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }
    ]

    return jsonify(random.choice(res))

if __name__ == '__main__':
    app.run()
