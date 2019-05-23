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
    disc = b**2 - 4 * a * c
    if disc >= 0:
        roots = [np.round((np.sqrt(disc) - b) / (2 * a), 3),
                 np.round((-np.sqrt(disc) - b) / (2 * a), 3)]
    else:
        roots = ['(imag)', '(imag)']
    return jsonify({'root_1': roots[0], 'root_2': roots[1]})
