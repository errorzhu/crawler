# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from db.dbclient import DbClient
import sys

sys.path.append('../')
app = Flask(__name__)

api_list = {
    'get': u'get an usable proxy',
}

@app.route('/')
def introduction():
    return jsonify(api_list)


@app.route('/get')
def get():
    db = DbClient()
    result = db.get()
    return result if result else 'no proxy!'


def run():
    app.run(host='0.0.0.0', port=9999, debug=True)


if __name__ == '__main__':
    run()
