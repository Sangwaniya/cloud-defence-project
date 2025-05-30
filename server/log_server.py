from flask import Flask, request

app = Flask(__name__)

@app.route("/logs", methods=["POST"])
def logs():
    print("Received log:", request.json)
    return "OK", 200

app.run(host="0.0.0.0", port=80)
