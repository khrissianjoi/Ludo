# server.py

import socket
import threading
import sys
from ludo import Game

ip_addr = '127.0.0.1'
port = 8000

print("server started")

# setup, 32bit ipv4, TCP/IP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_running = True

# give the socket an ip address and port
socket_details = (ip_addr, port)
serversocket.bind(socket_details)
serversocket.listen(100)

# store the connected devices
connected_devices = {}


def start_client_thread(connection, address):
    '''function to create thread'''
    th = threading.Thread(target=client_thread, args=(connection, address))
    th.start()
    connected_devices[connection]['thread'] = th
    print(currentGame)
    connection.send(currentGame)

def broadcast(message, original_conn):
    '''broadcast function, send data to all
    clients (except the original sender)'''
    # loop through connected devices
    # send data to connection
    for conn in connected_devices:
        if conn != original_conn:
            conn.send(message.encode(currentGame))


def client_thread(conn, addr):
    '''function to handle a client connection thread'''
    welcome = "Welcome to the chatroom"
    # unicode to bytes
    conn.send(welcome.encode())

    # if the client sends us data
    # send the data to every other client
    while server_running:
        try:
            # grab 1024 first bytes
            message = conn.recv(1024)
            if message is not None:
                # bytes turn to string
                enc_message = message.decode()
                message_to_send = "<{}> {}".format(addr, enc_message)
                print(message_to_send)
                broadcast(message_to_send, conn)
        except:
            continue


# main loop
# loop forever
# if there is a client waiting to connect
# make a thread for that client
# goto 1

currentGame = Game()
print(currentGame)
try:
    while True:
        conn, addr = serversocket.accept()
        connected_devices[conn] = {'addr': addr}
        print("{} connected".format(addr))
        # start thread for client connection
        start_client_thread(conn, addr)
except KeyboardInterrupt:
    print("Server shutting down")
    for conn in connected_devices:
        conn.close()
    serversocket.close()
    server_running = False
    print("Goodbye")
    sys.exit(0)