from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_it():
    params = request.json
    a = int(params['a_value'])
    b = int(params['b_value'])
    c = int(params['c_value'])
    ans = [(np.sqrt(b**2 - 4 * a * c) + s * b) / (2 * a) for s in [1, -1]]
    return jsonify({'values': ans})
