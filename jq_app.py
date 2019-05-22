from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('jq_index.html')

@app.route('/solve', methods=['POST'])
def solve_it():
    a, b, c = (request.json['a'],
               request.json['b'],
               request.json['c'])
    disc = np.sqrt(b**2 - 4 * a * c) * np.array([1, -1])
    roots = np.round((disc - b) / (2 * a), 3)
    return jsonify({'root_1': roots[0], 'root_2': roots[1]})
