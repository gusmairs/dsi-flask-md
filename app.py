from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_it():
    params = request.json
    a = params['a_value']
    b = params['b_value']
    c = params['c_value']
    return jsonify({'values': str(a) + str(b) + str(c)})
