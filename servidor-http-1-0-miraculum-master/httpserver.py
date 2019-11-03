"""
 Implementa um servidor HTTP/1.0 simples

"""

import socket
import htdocs
import os
import sys
#from htdocs import ipsum.html



# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('A ouvir na porta %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Handle client request
    request = client_connection.recv(1024).decode()
    z = request.split("\n")
    # Send HTTP response
    #response = '<HTTP/1.0 200 OK\n\n<h1>Olá mundo!</h1>\n'
    response = '<HTTP/1.0 200 OK\n\n'
    #for x in z:
    #    response += '<p>' + x + '</p>'

    with open(os.path.join(sys.path[0], "htdocs/index.html"), "r") as f:
        data = f.read()
        response += data
        f.close()

    print(response)
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
