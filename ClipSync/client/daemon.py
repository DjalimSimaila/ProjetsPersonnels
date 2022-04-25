import pyperclip
import socketio
# standard Python

# to put in a conf file
ip = 'lagrottedeneotaku.hopto.org'
port = "5000"
username = "Neotaku67"
hostname = "WarMachine"
logfilepath = "/home/djalim/logs.txt"

"""
This script is a daemon that, on event, send and sync the clipboard with a distant one
"""

sio = socketio.Client()
sio.connect(f"http://{ip}:{port}/")

@sio.event
def latest(data):
    print(data)
    print("")
    pyperclip.copy(data)

@sio.event
def test(data):
    print(data)

@sio.event
def all(data):
    print(data)

@sio.event
def device(data):
    print(data)

@sio.event
def id(data):
    print(data)

#to move elsewhere    
def emitEvent(event, value = "" ):
	sio.emit( event, {'hostname': hostname, "user" : username, "value" : value })

def test():
	sio.emit('all', {'hostname': hostname, "user" : username, "value" : '1er Copier Coller ou quoi la issou' })

sio.wait()
