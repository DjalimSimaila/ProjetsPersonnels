#!/bin/python
from flask import Flask, request, render_template, json, jsonify
import flask_socketio
# base socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test123'
app.config['FLASK_RUN_PORT'] = 5001


socketio = flask_socketio.SocketIO(app)

# Connection 

#flask_socketio.emit('latest',{"response" :  } )
@app.route("/notify", methods=['POST'])
def notify():
    data = {}
    data['title'] = request.form['title']
    data['content'] = request.form['content']
    print(data["content"],data["title"])
    socketio.emit("notify", data, broadcast=True)
    return "true" , 200

if __name__ == '__main__':
    socketio.run(app, port = 5001)
