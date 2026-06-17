from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_ai_response(query):
    return f"AI Research Summary\n\nTopic: {query}\n\nThis is a demo AI response."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query")

    response = generate_ai_response(query)

    return jsonify({
        "result": response
    })

if __name__ == "__main__":
    app.run(debug=True)
    