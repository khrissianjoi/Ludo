# client.py

import socket
import select
import sys
from ludo import Game


ip_address = '127.0.0.1'
port = 8000

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect((ip_address, port))
print("client connected")

# while true
# if we have data from the server, print it
# if we have data typed in by the user, send it

inputs = [sys.stdin, server_connection]

while True:
    try:
        # select which sockets have data
        # which inputs do we have data on
        read, write, error = select.select(inputs, [], [])
        for data_input in read:
            if data_input == server_connection:
                message = data_input.recv(1024)
                parsed_message = message.decode()
                if parsed_message != '':
                    # if we have data from the server, print it
                    print(parsed_message)
            else:
                # we are getting data from the keyboard
                message = sys.stdin.readline()
                server_connection.send(message.encode())
                # print out what the user types back to them
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()

    except KeyboardInterrupt:
        server_connection.close()
        print("Disconnected")