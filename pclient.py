#Player Client
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1 \r\n",4000))
s.send("Hello\r\n".encode())
greet=s.recv(80).decode()
print(greet)
if(greet=="Greetings\r\n"):
    s.send("Game\r\n".encode())
    g=s.recv(80).decode()
    print(g)
    if(g=="Ready\r\n"):
        while(g!="Correct\r\n"):
            guess=input("Guess a number between 1 and 30: ")
            #test the user input and make sure its a valid number
            try:
                Test=int(guess)
            except ValueError:
                print("Please insert a valid number?")
            else:
                send=("My Guess is: "+guess+"\r\n")
                s.send(send.encode())
                g=s.recv(80).decode()
                if(g=="Correct\r\n"):
                    print("Congratulations you have won!\r\n")
                    s.close()
                elif(g=="Far\r\n"):
                    print("You are far off, try again\r\n")
                elif(g=="Close\r\n"):
                     print("You are getting close try again\r\n")
                else:
                     print("Unexpected response from server!\r\n")
