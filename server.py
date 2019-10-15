import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server socket is created")
host = "192.168.43.180"
#host = socket.gethostbyname(socket.gethostname())
port = 12345

server_socket.bind((host,port))
print("Server socket is created at ip {} and port {}".format(host,port))

server_socket.listen()
print("The server is ready to listen")

client_socket,client_addr = server_socket.accept()
print(client_socket)
print(client_addr)
while True:
    smsg = input("Server : ")
    client_socket.send(smsg.encode())
    if smsg.strip().lower() == "bye":
        print("Connection is closed by server")
        client_socket.close()
        server_socket.close()
        break
    cmsg = client_socket.recv(1024)
    print("Client : ",cmsg.decode())
    if cmsg.decode().strip().lower() == "bye":
        print("Connection is closed by client")
        client_socket.close()
        server_socket.close()
        break

