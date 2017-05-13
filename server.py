#Server
import threading
import socket
import random


socks = []

#Define function to handle client interaction
def handle_client(conn,addr):
    socks.append(addr)
    xx=conn.recv(80).decode()
    if(xx=="Hello\r\n"):
        conn.send("Greetings\r\n".encode())
        xx=conn.recv(80).decode()
        if(xx=="Game\r\n"):
            conn.send("Ready\r\n".encode())
            bool1=True
            rnd=random.randrange(1,31)
            while(bool1):
                try: 
                    guess=conn.recv(80).decode()
                except:
                    break
                #splits incoming guess and takes value 3 (aka the number)
                split=guess.split(" ")
                guess1=split[3]
                #test incoming guess and make sure its a valid number or return "far" to the client
                try:
                    N=int(split[3])
                except ValueError:
                    conn.send("Far\r\n".encode())
                else:   
                    if(N==rnd):
                        conn.send("Correct\r\n".encode())
                        bool1=False
                     #   del stAddr
                        #remove apended addr
                    elif(N<(rnd+3)and N>(rnd-3)):
                        conn.send("Close\r\n".encode())
                    else:
                        conn.send("Far\r\n".encode())
            del socks[-1]
            conn.close()

#Define function to handle Admin interaction
def handle_admin(conn,addr):
    try:
        xx=conn.recv(80).decode()
    except:
        conn.close()
    if(xx=='Hello\r\n'):
        conn.send("Admin-Greeatings\r\n".encode())
        xx=conn.recv(80).decode()
        if(xx=="Who\r\n"):
            Send_socks()

#since you cant encode socket info diectly i made another list
#that gets wiped each time i run this function, it casts the addr(address)
#from the list of addresses, to a new list of strings, then joins them into
#a single long string and fixes formatting issues and finally sends the string
#to the admin client
def Send_socks():
    stAddr = []
    for addr in socks:
        strItem=str(addr)
        stAddr.append(strItem)
    fixMe = '\r\n'.join(map(str, stAddr))
    fixMe = fixMe.replace("(", "")
    fixMe = fixMe.replace(")", "")
    fixMe = fixMe.replace("'", "")
    fixMe = fixMe.replace(",", "")
    sendMe = fixMe
    conn.send(sendMe.encode())


#function to create a new thread to handle client           
def Accept_Client():
    while True:
        (conn,addr) = s1.accept()       
        t = threading.Thread(target = handle_client, args = (conn,addr))
        t.start()
        
#here is where shit starts
TCP_IP="127.0.0.1 \r\n"
TCP_PORT=4000
Admin_PORT=4001
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind((TCP_IP,TCP_PORT))
s2.bind((TCP_IP,Admin_PORT))
s1.listen(5)
s2.listen(5)


#t1 is the client thread  
t1 = threading.Thread(target = Accept_Client, args = ())
t1.start()
#admin client will only be one at any time

#t2 is admin thread
while True:
    (conn,addr) = s2.accept()
    t2 = threading.Thread(target = handle_admin, args = (conn,addr))
    t2.start()
    
