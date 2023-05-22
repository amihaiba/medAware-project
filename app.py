# Description: An app that receive a POST request and send the content of a specified file to a db and as a response
#             to the request, and if the request contains 'id_db': true, move the specified file from the 'staging'
#             directory to a 'done' directory

import os
from flask import Flask, request, jsonify
import mysql
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def request_handler():
    """Handle entering requests, read their content and perform needed actions"""
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request'}), 400
    is_db = request.json.get('is_db')
    file_name = request.json.get('file_name')
    if not os.path.isfile('staging/' + file_name):
        return jsonify({'error': 'File does not exist'}), 400
    response = response_handler(file_name)
    if is_db:
        db_handler(file_name)
        archiver(file_name)
    return response


def response_handler(file_name):
    """Handle sending response to requests"""
    with open('staging/' + file_name, 'r') as f:
        content = f.read()
        return jsonify({f"{file_name}": content})


def db_handler(file_name):
    """Handle interface with the database"""
    pass


def archiver(file_name):
    """Move specified file from staging dir to done dir"""
    os.rename('staging/' + file_name, 'done/' + file_name)


if __name__ == "__main__":
    """Tests can be added here"""
    app.run(debug=True)
