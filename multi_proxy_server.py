import socket
import sys
import time
from multiprocessing import Process
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_request(conn,addr,proxy_end):
    request_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    proxy_end.sendall(request_data)
    proxy_end.shutdown(socket.SHUT_WR)

def main():
    host = 'www.google.com'
    port = 80

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(10)

        while True:
            conn,addr = proxy_start.accept()
            print("Connected by",addr)
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                try:
                    remote_ip = socket.gethostbyname( host )
                except socket.gaierror:
                    print ("Hostname could not be resolved. Exiting")
                    sys.exit()

                proxy_end.connect((remote_ip,port))
                p = Process(target = handle_request, args = (conn,addr,proxy_end))
                p.daemon = True
                p.start()
                print("start processing")
            conn.close()

if __name__ == "__main__":
    main()

