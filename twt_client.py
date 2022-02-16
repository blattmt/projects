from http import client
import socket

from twt_server import DISCONNECT_MSG

HEADER = 64
PORT = 12000
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'
SERVER = '192.168.0.2'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)