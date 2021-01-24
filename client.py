import socket
import sys

try:
    # define address info, payload, and buffer size
    host = 'www.google.com'
    port = 80
    # get request from google
    payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    buffer_size = 4096

    # create the socket, get the ip, and connect
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    # get remote ip 
    
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()
    
    print (f'Ip address of {host} is {remote_ip}')
    s.connect((remote_ip , port))
    print (f'Socket Connected to {host} on ip {remote_ip}')
    
    # send the data and shutdown
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")
    s.shutdown(socket.SHUT_WR)

    # accept the data
    full_data = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
             break
        full_data += data
    print(full_data)

except Exception as e:
    print(e)
finally:
    s.close()




