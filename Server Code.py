import socket
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket is succesfully created..!')

port = 5555
Host='127.0.0.1'
serversocket.bind((Host, port))
print('Sucessfully binded..! ')
serversocket.listen(5)
print('Started listening...')


clients=[]


#Thread is created 

def Handle(client,username):
    
    while True:
        
        try: 
            #server is receiving the data from client
            data=client.recv(1024).decode('utf-8')
            receiver=client.recv(1024).decode('utf-8')
            sending(data,receiver,client,username)
        except:
            # if the client left, remove the name and the data.
            index = clients.index(client)
            clients.remove(client)
            client.close()
            print('{} left the conversation..!'.format(username))
            clients.remove(username)
            break       

#Server is sending the data to the client
def sending(data,receiver,client,username):
    try:
        index = clients.index(receiver)
        RecvClient=clients[index+1]
        RecvClient.sendall(data.encode('utf-8'))
    except:
        data=('The entered name is not present at the moment. The online users are: '.encode('ascii'))
        client.sendall(data)
        length=len(clients)
        i=0
        for x in range(length):
            try:
                usernamesList=('{} \n'.format(clients[x+i]))
                client.sendall(usernamesList.encode('utf-8'))
                i=i+1
            except:
                break

    

             
#waiting for the connections to accept      
while True:
    client,Addr = serversocket.accept()
    print("connected with {}".format(str(Addr)))
    client.send('Username'.encode('utf-8'))
    username=client.recv(1024).decode('utf-8')
    clients.append(username)
    clients.append(client)
    length=len(clients)
    i=0
    for x in range(length):
        try:
            usernamesList=('{} \n'.format(clients[x+i]))
            client.sendall(usernamesList.encode('utf-8'))
            i=i+1
        except:
            break

    #creating a thread
    threading._start_new_thread(Handle, (client,username))
    
