import socket
import http.client

HOST = "172.20.10.7"
PORT = 8888
test_case = 0

while(1):
    print ("1. GET TEST\n2. HEAD TEST\n3. POST TEST\n4. PUT TEST\n5. DELETE TEST\n6. END THE TEST")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect((HOST, PORT))
        test_case = int(input())
        if test_case == 1:
            server.sendall(b"GET TEST.html")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
        elif test_case == 2:
            server.sendall(b"HEAD TEST.html")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
        elif test_case == 3:
            server.sendall(b"POST TEST.html MADE IN JUNYOUNG")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
            server.sendall(b"MADE IN JUNYOUNG")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
        elif test_case == 4:
            server.sendall(b"PUT TEST.html MADE BY JUNYOUNGPARK 20181620")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
        elif test_case == 5:
            server.sendall(b"DELETE TEST.html")
            recieve_data = server.recv(65535)
            print(recieve_data.decode()+"\n")
        elif test_case == 6:
            print("FINISH THE TEST")
            server.sendall(b"END")
            break
        else:
            print ("입력한 숫자를 다시 확인해주십시오.")
                
    server.close()
