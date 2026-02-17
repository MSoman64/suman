from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_poem(topic):
    lines = [
        f"{topic} is a whisper in the night,",
        f"{topic} shines in soft moonlight,",
        f"{topic} dances with my soul,",
        f"{topic} makes the broken whole,",
        f"In dreams of {topic}, I stay,",
        f"{topic} guides me on my way."
    ]

    poem = random.sample(lines, 4)
    return "\n".join(poem)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data["message"]

    poem = generate_poem(user_msg)
    return jsonify({"reply": poem})

if __name__ == "__main__":
    app.run(debug=True)
