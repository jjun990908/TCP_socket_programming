import socket
from os.path import exists, getsize
from os import remove

HOST = "172.20.10.7"
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("START THE SERVER")

    while(1):
        connection_socket, addr = server.accept()
        msg = connection_socket.recv(65535).decode()
        request_data = msg.split()
        request_method = request_data[0]
        if msg == "END":
            print("END THE SERVER")
            connection_socket.close()
            break
        filepath = './' + msg.split()[1]
        filetype = msg.split()[1].split('.')[1]
        filename = msg.split()[1].split('.')[0]
    
        if request_method == "GET":
            if not exists(filepath):
                print("오류 발생(GET)")
                msg = "HTTP/1.0 404 NOT FOUND\r\nHost:172.20.10.7"
                connection_socket.sendall(msg.encode())
            else:
                size = getsize(filepath)
                print(msg)
                msg = "HTTP/1.0 200 OK\r\nHOST:172.20.10.7\r\n"
                with open(filepath, 'r') as file:
                    data = ''
                    for line in file:
                        data += line
                connection_socket.send(msg.encode())
                connection_socket.send(data.encode())
                
        elif request_method == "HEAD":
            if not exists(filepath):
                print("오류 발생(HEAD)")
                msg = "HTTP/1.0 404 NOT FOUND\r\nHost:172.20.10.7"
                connection_socket.sendall(msg.encode())
            else:
                size = getsize(filepath)
                print(msg)
                msg = "HTTP/1.0 200 OK\r\nHOST:172.20.10.7"
                connection_socket.send(msg.encode())
                
        elif request_method == "POST":
            print(msg)
            f = open(filename+'.'+filetype,'w')
            msg = "HTTP/1.0 100 OK\r\nHOST:172.20.10.7"
            connection_socket.send(msg.encode())
            msg = connection_socket.recv(65535).decode()
            for i in msg:
                f.write(i)
            f.close()
            msg = "HTTP/1.0 201 OK\r\nHOST:172.20.10.7"
            connection_socket.send(msg.encode())

        elif request_method == "PUT":
            if not exists(filepath):
                print("오류 발생(PUT)")
                msg = "HTTP/1.0 404 NOT FOUND\r\nHost:172.20.10.7"
                connection_socket.sendall(msg.encode())
                connection_socket.close()
            else:
                print(msg)
                f = open(filename+'.'+filetype,'w')
                for i in msg.split()[2:]:
                    f.write(i+" ")
                f.close()
                msg = "HTTP/1.0 201 OK\r\nHOST:172.20.10.7"
                connection_socket.send(msg.encode())
                
        elif request_method == "DELETE":
            if not exists(filepath):
                print("오류 발생(REMOVE)")
                msg = "HTTP/1.0 404 NOT FOUND\r\nHost:172.20.10.7"
                connection_socket.sendall(msg.encode())
                connection_socket.close()
            else:
                print(msg)
                remove(filepath)
                msg = "HTTP/1.0 204 OK\r\nHOST:172.20.10.7"
                connection_socket.send(msg.encode())
                
        else:
                msg = "HTTP/1.0 400 WRONG REQUEST\r\nHOST:172.20.10.7"
                connection_socket.send(msg.encode())
