import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

server_socket.connect((host,port))

while True:
    smsg = server_socket.recv(1024)
    print("Server : ",smsg.decode())
    if smsg.decode().strip().lower() == "bye":
        print("Connection is closed by server")
        server_socket.close()
        break
    cmsg = input("Client : ")
    server_socket.send(cmsg.encode())
    if cmsg.strip().lower() == "bye":
        print("Connection is closed by client")
        server_socket.close()
        break
