import socket               # Import socket module

_s = socket.socket()         # Create a socket object
#host = "192.168.1.2" # Get local machine name
#port = 58012                # Reserve a port for your service.


def receiveFile(s, _host, _port):
    s.bind((_host, _port))  # Bind to the port
    f = open('out_text.txt', 'wb')
    s.listen(5)
    while True:
        c, addr = s.accept()  # Establish connection with client.
        print('Got connection from', addr)
        print("Receiving...")
        l = c.recv(1024)
        while l:
            print("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("Done Receiving")
        # c.send('Thank you for connecting')
        c.close()
        break

