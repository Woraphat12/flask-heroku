from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask-Herok"

if __name__ == "__main__":
    app.run(debug=False)
