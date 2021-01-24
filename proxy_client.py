import socket
import sys

def main():
	host = "127.0.0.1"
	port = 8001
	buffer_size = 4096
	payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except (socket.error, msg):
	    print(f"Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}")
	    sys.exit()

	s.connect((host,port))
	print (f"Socket Connected to {host}")
	# send the data and shutdown
	s.sendall(payload.encode())
	s.shutdown(socket.SHUT_WR)
	
	
	full_data = s.recv(buffer_size)
	print(full_data)

	s.close()

if __name__ == "__main__":
	main()