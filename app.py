# Description: An app that receive a POST request and send the content of a specified file to a db and as a response
#             to the request, and if the request contains 'id_db': true, move the specified file from the 'staging'
#             directory to a 'done' directory

import os
from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def request_handler():
    """Handle entering requests, read their content and perform needed actions"""
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request'}), 400
    is_db = request.json.get('is_db')
    file_name = request.json.get('file_name')
    if not os.path.isfile('staging/' + file_name):
        return jsonify({'error': 'File not found'}), 400
    response = response_handler(file_name)
    if is_db:
        status_code = db_handler(file_name)
        if status_code != "success":
            return jsonify({'error': str(status_code)}), 400
        archiver(file_name)
    return response


def response_handler(file_name):
    """Handle sending response to requests"""
    with open('staging/' + file_name, 'r') as f:
        content = f.read().strip('\n')
        return jsonify({f"{file_name}": content})


def db_handler(file_name):
    """Handle interface with the database"""
    # Read specified file's contents
    with open('staging/' + file_name, 'r') as f:
        content = f.read().strip('\n')
    # Connect to MySQL database to insert a record, handle connection and duplicate key errors
    try:
        med_db = mysql.connector.connect(
            host='mysql',
            user='root',
            password='root',
            database='med_db'
        )
        db_cursor = med_db.cursor()
        # Set MySQL command to be used
        sql = "INSERT INTO med_records (file_name, file_content) VALUES (%s, %s)"
        # Set MySQL command parameters
        val = (file_name, content)
        db_cursor.execute(sql, val)
        med_db.commit()
        # Close connection to MySql database
        if med_db.is_connected():
            med_db.close()
        if db_cursor:
            db_cursor.close()
        return "success"
    except mysql.connector.Error as err:
        return err


def archiver(file_name):
    """Move specified file from staging dir to done dir"""
    os.rename('staging/' + file_name, 'done/' + file_name)
    return "success"


if __name__ == "__main__":
    """Tests can be added here"""
    app.run(debug=True)
