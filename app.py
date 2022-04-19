from flask import Flask, request, url_for, redirect, render_template, jsonify
import json

app =Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/manual')
def manual():
    return render_template('game-manual/index.html')

@app.route('/automatic')
def automatic():
    return render_template('game/index.html')


if __name__ == '__main__':
    app.run()