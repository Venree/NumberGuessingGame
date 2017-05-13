#Admin Client
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1 \r\n",4001))
s.send("Hello\r\n".encode())
greet=s.recv(80).decode()
if(greet=="Admin-Greeatings\r\n"):
    s.send("Who\r\n".encode())
    print("The IP and ports of the connected clients are:\n")
    while True:
        try:
            g=s.recv(800).decode()
        except:
            break
    
        print(g)
        s.close()
