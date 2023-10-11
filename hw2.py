# import socket

# # Define the server's host and port
# HOST = '192.168.56.1'
# PORT = 443

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the host and port
# server_socket.bind((HOST, PORT))

# # Listen for incoming connections
# server_socket.listen(5)
# print(f"Server is listening on {HOST}:{PORT}")

# while True:
#     # Accept a connection from a client
#     client_socket, client_address = server_socket.accept()
#     print(f"Accepted connection from {client_address}")

#     while True:
#         # Receive data from the client
#         data = client_socket.recv(1024)
#         print(data)
#         if not data:
#             # If no data is received, the client has closed the connection
#             break

#         # Echo the received data back to the client
#         client_socket.send(data)

#     # Close the client socket
#     client_socket.close()
#     print(f"Connection with {client_address} closed")
import socket
import numpy as np
import json
import time
import random
import matplotlib.pyplot as plt
HOST = '192.168.162.246' # IP address 
PORT = 42342 # Port to listen on (use ports > 1023)
datalistx=[]
datalisty=[]
datalistz=[]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while(1):

            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024).decode('utf-8')
                    print(data)
                    
                    arr=list(map(int,data.split()))
                    datalistx.append(arr[0])
                    datalisty.append(arr[1])
                    datalistz.append(arr[2])
                    plt.ion()
                    # plt.subplots()
                    plt.clf()
                    plt.plot(datalistx)
                    plt.plot(datalisty)
                    plt.plot(datalistz)
                    plt.pause(0.001)
                    
                    # plt.show()




                    

