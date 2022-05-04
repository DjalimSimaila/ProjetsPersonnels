import pyperclip
import socketio
import os
# standard Python

# to put in a conf file
ip = 'lagrottedeneotaku.hopto.org'
port = "5001"
hostname = "WarMachine"
logfilepath = "./logs.txt"

"""
This script is a daemon that, on event, send and sync the clipboard with a distant one
"""

commad = f"http://{ip}:{port}/"
print(commad)

sio = socketio.Client()
sio.connect(f"http://{ip}:{port}/")

@sio.event
def notify(data):
    title, content = data["title"], data["content"]
    command = f'notify-send "{title}" "{content}"'
    print(command)
    os.system(command)
    

sio.wait()
