import socket
import sys
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():
	host = "www.google.com"
	port = 80
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_start:
		
		proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		proxy_start.bind((HOST,PORT))
		proxy_start.listen(10)
		
		while True:
			conn,addr = proxy_start.accept()
			print("Connected by",addr)
			with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:	
				print(f"Getting IP for {host}")
				try:
					remote_ip = socket.gethostbyname(host)
				except socket.gaierror:
					print("failed to get ip")
					sys.exit()

				proxy_end.connect((remote_ip,port))
				
				# send the data and shutdown
				full_data = conn.recv(BUFFER_SIZE)
				time.sleep(0.5)
				print("Send the data to google: ",full_data)
				proxy_end.sendall(full_data)
				proxy_end.shutdown(socket.SHUT_WR)
				
				client_data = proxy_end.recv(BUFFER_SIZE)
				time.sleep(0.5)
				print("Send the data to client: ",client_data)
				conn.sendall(client_data)
			conn.close()  

if __name__ == "__main__":
    main()