import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'
PORT = 12000
#get ip address by hostname in lieu of hardcoding
SERVER = socket.gethostbyname(socket.gethostname())
#Creating ip/port tuple
ADDR = (SERVER,PORT)

#make socket object using IPv4 and TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind using current info
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        #Receive first message, telling how many byte to receive, and decode
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            #cast to int so we have an actual value and not a string
            msg_length = int(msg_length)
            #look for actual message of previously prescribed length and decode
            msg = conn.recv(msg_length).decode(FORMAT)
            #Check is message is telling server to disconnect, if so change sentinal value to end loop
            if msg == DISCONNECT_MSG:
                connected = False
            #display message and it's source ip
            print(f'[{addr}] {msg}')
    #close connection
    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        #blocks, waiting for a new connection and will store connection info into socket: conn, (ip/port): addr
        conn, addr = server.accept()
        #Once new connection is established, start new thread to handle client connection using tuple we just received
        #Create the thread
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        #start thread
        thread.start()
        #Message to show number of threads/connections
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() -1}')

print('[STARTING] Server is starting...')
start()
