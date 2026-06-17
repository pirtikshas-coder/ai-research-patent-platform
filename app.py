from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

def generate_ai_response(query):

    return f"""
Topic:
{query}

Summary:
{query} is an emerging research field.

Applications:
• Healthcare
• Industry
• Education
• Artificial Intelligence

Future Scope:
Strong growth expected.
"""

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route(
"/search",
methods=["POST"]
)

def search():

    data = request.json

    query = data.get(
        "query"
    )

    result = generate_ai_response(
        query
    )

    return jsonify({

        "result":
        result

    })

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
    