from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/like", methods=["GET"])
def like():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({
            "success": False,
            "message": "UID not provided"
        }), 400

    before = random.randint(10, 100)
    after = before + random.randint(1, 10)

    return jsonify({
        "success": True,
        "uid": uid,
        "likes_before": before,
        "likes_after": after
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
