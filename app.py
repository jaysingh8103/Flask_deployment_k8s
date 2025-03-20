from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Get MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["taskmanager"]
tasks_collection = db["tasks"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_task():
    data = request.json
    if "task" not in data:
        return jsonify({"error": "Task is required"}), 400

    tasks_collection.insert_one({"task": data["task"]})
    return jsonify({"message": "Task added successfully"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return jsonify(tasks)

@app.route("/delete", methods=["POST"])
def delete_task():
    data = request.json
    if "task" not in data:
        return jsonify({"error": "Task is required"}), 400

    tasks_collection.delete_one({"task": data["task"]})
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
