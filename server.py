import socket
from threading import Thread

server = None 
port = None
ip = None

clients = {}
def acceptConnections():
    global server
    global clients
    while True:
        playersocket, addr = server.accept()
        playername = playersocket.recv(1024).decode().strip()
        if(len(clients.keys()) == 0):
            clients[playername] = {'playertype' : 'player1'}
        else:
            clients[playername] = {'playertype': 'player2'}
        clients[playername]["playersocket"] = playersocket
        clients[playername]["address"] = addr
        clients[playername]["playername"] = playername
        clients[playername]["turn"] = False

        

def setup():
    global server
    global port
    global ip
    ip = '127.0.0.1'
    port = 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen()
    acceptConnections()




setup()