#Create a simple HTML Flask Application that displays a welcome message
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return ("WELCOME TO BEVERLY'S WEBSITE")

if __name__ == '__main__':
    app.run(debug=True)
