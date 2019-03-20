import json

from flask import Flask, request, jsonify

from KB_query.generate_sparql import generate_sparql

app = Flask(__name__)


@app.route('/get_sparql', methods=["POST"])
def get_sparql():
    data = json.loads(request.get_data())
    rs = generate_sparql(data['q'])

    return jsonify(code=200, message='ok', data={'sparql': rs})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
