from flask import Flask, jsonify

app = Flask(__name__)

TASKS = [
    {"id": 1, "title": "Make app", "done": False},
    {"id": 2, "title": "Make bapp", "done": True},
]


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "APi works", "endpoints": ["/tasks"]})


app.route("/tasks", methods=["GET"])


def get_tasks():
    return jsonify(TASKS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
