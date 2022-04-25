#!/bin/python
from flask import Flask
import flask_socketio
import sql
# base socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test123'
socketio = flask_socketio.SocketIO(app)

# Connection 

#flask_socketio.emit('latest',{"response" :  } )

@socketio.on('test')
def handle_message(data):
    print(sql.getIdDev('AAAA'))
    flask_socketio.emit('test', {'response': "recu .w."})

@socketio.on('add')
def add(data):
    print(f"{data['user']} has made a 'add' event")
    flask_socketio.emit('latest',ClipBoard(data["user"]).setNewValue(data["value"],data["hostname"]),broadcast = True)

@socketio.on('latest')
def lastest(data):
    print(f"{data['user']} has made a 'latest' event")
    flask_socketio.emit('latest',str(ClipBoard(data["user"]).getLatestValue()))

@socketio.on('all')
def getAll(data):
    print(f"{data['user']} has made a 'all' event")
    flask_socketio.emit('all', str(ClipBoard(data["user"]).getAll()))

@socketio.on('byId')
def byid(data):
    print(f"{data['user']} has made a 'byId' event")
    flask_socketio.emit('id',str(ClipBoard(data["user"]).getById(data["value"])))

@socketio.on('byHostname')
def lastest(data):
    print(f"{data['user']} has made a 'byHostname' event")
    flask_socketio.emit('device',str(ClipBoard(data["user"]).getByDevice(data["value"])))


if __name__ == '__main__':
    socketio.run(app)
