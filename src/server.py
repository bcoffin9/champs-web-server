from socket import *
import threading
from client_handler import client_thread  # Importing client_thread function

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Set the SO_REUSEADDR option
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    ct = threading.Thread(target=client_thread, args=(connectionSocket, addr))
    ct.start()
