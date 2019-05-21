from flask import Flask, request, render_template, jsonify
# import numpy as np

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('jq_index.html')

@app.route('/solve', methods=['POST'])
def solve_it():
    a = request.json
    return jsonify({'a': a})

    # params = request.json
    # a, b, c = (params['a_value'],
    #            params['b_value'],
    #            params['c_value'])
    # ans = [(np.sqrt(b**2 - 4 * a * c) + s * b) / (2 * a) for s in [1, -1]]
    # return jsonify({'values': [round(i, 3) for i in ans]})
