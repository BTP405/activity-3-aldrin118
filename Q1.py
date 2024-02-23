#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.

import socket
import pickle

def run_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #set up the socket connections
        server_address = ('localhost',12345)
        server_socket.bind(server_address)
        server_socket.listen(1)
    except: #when an error when setting up the server settings
        print("An error occured when setting up the server")


    print("Server is listening for incoming connection")

    while True:
        client_socket, client_address = server_socket.accept() #accept the connection

        try:
            print("Connected to:" , client_address)

            data = client_socket.recv(1024) #recieve data from the client
            f = open("./files/demofile2.txt", "x") #creating the file sent by the client
            f.write(pickle.loads(data)) #unpickle and write the pickled file sent by the client
            f.close() #close the file

            message = "Message recieved by the server!"
            client_socket.sendall(message.encode()) #send a message back to the client that the file has been recieved

        finally:
            client_socket.close()

def run_client():

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates the connection to the server
        server_address = ('localhost',12345)
        client_socket.connect(server_address)
    except: #prints an error if thier is a connection problem
        print("error occured while connecting to the server")

    try:
        file = open("testing.txt" , "x") #creates the file that needs to be sent
        file.write("testing data to pickeled \n and sends") #writing into the file
        file.close()
        f = open("testing.txt" , "r") #open the created file
        data = f.read() # read the data from the file
        client_socket.send(pickle.dumps(data , protocol = 5)) #send the data to the server while also pickleing it
        f.close() #close te file

        data = client_socket.recv(1024) #recieve the message from the server
        print("Recieved from server:", data) #prints the data

    finally:
        client_socket.close() #close the connection to the server

#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.
