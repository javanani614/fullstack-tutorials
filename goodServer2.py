import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5000))
print "Web server running..."
server_sock.listen(10)
inputfile = open('TestFile.txt')
while True:
    client_sock, addr = server_sock.accept()
    client_sock.send("HTTP/1.1 200 OK\n")
    #client_sock.send("Content length: "+str(len(output)))
    client_sock.send("Content-Type: text/html\n\n")
    print 'We have opened a socket!'
    print client_sock.recv(1024)  # these are the incoming headers
    output = "<h1>Hello Client</h1>"
    client_sock.send(output)
    for line in inputfile:
    	output = line + "<br />"
    	client_sock.send(output)
    inputfile.close()
    client_sock.close()