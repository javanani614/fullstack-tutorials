import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('HOST', 5015))
print "Web server running..."
server_sock.listen(1)

while True:
    client_sock, addr = server_sock.accept()
    saveSock = "GET HTTP/1.1 200 ok       HOST:http:localhost:5000/kittens"
    saveSock2 = str(client_sock.recv(1024))
    saveSock = saveSock2
    #print saveSock
    listOfPaths = saveSock.split('/')
    print len(listOfPaths)
    client_sock.send("HTTP/1.1 200 OK\n")
    #client_addr = client_sock.recv(1024) 
	#client_sock.send("Content length: "+str(len(output)))
	#findPath(client_addr)
	#cachePaths = client_addr

    client_sock.send("Content-Type: text/html\n\n")
    print 'We have opened a socket!'
    #saveSock = client_sock.recv(1024)  # these are the incoming headers
    isKittenPath = False
    theFile = 'TestFile.txt'
    for path in listOfPaths:
    	if path.find("kittens") == True:
    		isKittenPath = True
		
	if isKittenPath: 
		theFile = "<h3>TestKittenFile.txt</h3>"
	else:
		theFile = "<h3>TestFile.txt</h3>"

    client_sock.send(theFile)
    
    #inputfile.close()
    client_sock.close()