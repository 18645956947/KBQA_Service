import json

from flask import Flask, request, jsonify, render_template

from KB_query.generate_sparql import generate_sparql

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/get_sparql', methods=["POST"])
def get_sparql():
    rs = generate_sparql(request.form.get('q'))

    return jsonify(code=200, message='ok', data={'sparql': rs})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
