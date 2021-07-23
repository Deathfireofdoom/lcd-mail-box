import psycopg2
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

from mailboxlcd import display_message





app = Flask(__name__)

@app.route('/api/mailbox', methods=['POST'])
def leave_message():
    data = request.json
    display_message(data)
    


    return {'hej':'hej'}










if __name__ == '__main__':
    app.run()