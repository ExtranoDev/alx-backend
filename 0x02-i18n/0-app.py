#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Displays value to html page"""
    title = 'Welcome to Holberton'
    body = 'Hello world'
    return render_template('0-index.html', title=title, body=body)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
