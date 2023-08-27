#!/usr/bin/env python3
"""
Simple flask app implementation
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """renders an html page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
