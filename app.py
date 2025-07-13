from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection (use localhost for local MongoDB)
client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["events"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")
    author = data.get("sender", {}).get("login", "Unknown")
    timestamp = datetime.utcnow().strftime('%d %b %Y - %I:%M %p UTC')
    message = ""

    if event_type == "push":
        to_branch = data.get("ref", "").split("/")[-1]
        message = f"{author} pushed to {to_branch} on {timestamp}"

    elif event_type == "pull_request":
        action = data.get("action")
        if action in ["opened", "synchronize"]:
            from_branch = data.get("pull_request", {}).get("head", {}).get("ref", "")
            to_branch = data.get("pull_request", {}).get("base", {}).get("ref", "")
            message = f"{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}"

    elif event_type == "merge_group":
        from_branch = data.get("merge_group", {}).get("head_ref", "")
        to_branch = data.get("merge_group", {}).get("base_ref", "")
        message = f"{author} merged branch {from_branch} to {to_branch} on {timestamp}"

    if message:
        collection.insert_one({
            "message": message,
            "timestamp": timestamp
        })

    return jsonify({"status": "ok"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0, "message": 1}).sort("timestamp", -1).limit(10))
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
