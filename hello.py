from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask import request

from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/test/", methods=['get'])
def test():
    content = {
        "name": "python test flask server",
        "datetime": datetime.now()
    }
    return jsonify(content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)