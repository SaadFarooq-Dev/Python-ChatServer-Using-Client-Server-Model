import socket
import threading

username=input("Enter your name: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555
Host='127.0.0.1'
client.connect((Host, port))
print('Succesfully connected..!')
print("Users Online At the moment: \n")




def receive(client):
    while True:
        try:
            # receiving the messages from the server
            message = client.recv(1024).decode('utf-8')
            if message == 'Username':
                client.send(username.encode('utf-8'))
            else:
                print(message,end="\n")
        except:
            # if the server leaves, then close the connection
            print("An error has occured the host might be down at the moment please try again!")
            client.close()
            break


# sending the messages to the server
def senddata(client):
    while True:
        print('\n')
        print('{}:'.format(str(username)))
        message = '{}:{}'.format(username, input(''))
        client.send(message.encode('utf-8'))
        print("\nEnter the name of the person you want to send message: ")
        message=input('')
        client.send(message.encode('utf-8'))
        

# thread is created to receive and send data
threading._start_new_thread(receive, (client,))
threading._start_new_thread(senddata, (client,))

