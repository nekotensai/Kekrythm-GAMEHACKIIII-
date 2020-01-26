# from flask import Flask, request
# from tinydb import TinyDB, Query
# import json
#
# app = Flask(__name__)
# db = TinyDB('db.json')
#
# @app.route('/', methods=['POST'])
# def parse_request():
#     jso = json.loads(request.json)
#     name = jso['name']
#     points = jso['points']
#     db.insert({'name':name,'points':points})
#     return 'kek'
#
# @app.route('/table')
# def kek():
#     s = 'История игр: '
#     for i in db.all():
#         s += i['name'] + ' ' + str(i['points']) + ';  '
#     return s
#
# if __name__ == "__main__":
#     app.debug = True
#     app.run()
