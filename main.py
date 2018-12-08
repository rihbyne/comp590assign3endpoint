from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    welcome = {'project': 'comp590, android HTTP loopers/handlers, assign3'}
    return jsonify(welcome), 200


@app.route('/hockeyteams', methods=['GET'])
def hockeylist():
    hockey_data = None
    with open('data.json', 'r') as f:
        hockey_data = json.load(f)
    return jsonify(hockey_data), 200


@app.errorhandler(404)
def not_found(error):
    msg_trace = "url not found: %s." % (request.path)
    error_msg = {'failed': msg_trace}
    app.logger.error(error_msg)
    return jsonify(error_msg), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
