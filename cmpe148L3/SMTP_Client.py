import socket

msg = ("\r\n I love computer networks!")
endmsg = ("\r\n.\r\n")

# Choose a mail server (e.g. Google mail server) and call it mailserver
#found a server hosted on cloud for SMTP email testing "mailosaur"
mailserver = ("smtp.mailosaur.net", 2525)
	
#Create socket called clientSocket and establish a TCP connection with mailserver
print ("TCP connection")
clientSocket = socket.socket()
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != "220":
    print("220 reply not received from server.")
	
#send HELO command and print server response.
print ("Helo Command")
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != "250":
    print("250 reply not received from server.")
	
#send MAIL FROM command and print server response.
print ("Mail From")
mailCommand = "MAIL FROM:syed@gmail.com\r\n"
clientSocket.send(mailCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print (recv2)
if recv2[:3] != "250":
    print("250 reply not received from server.")

# Send RCPT TO command and print server response.
print ("\nRCPT TO")
rcptCommand = "RCPT TO:rhonel@wx6ju06h.mailosaur.net\r\n"
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print (recv3)
# server used doesn't return typical 250 code rather returns specified email 
# if recv3[:3] != "250":
#     print ("250 reply not received from server.1")
	
# Send DATA command and print server response.
print ("DATA")
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print (recv4)
if recv4[:3] != "250":
    print ("250 reply not received from server")
	

# Send message data.
print ("Message Data")
clientSocket.send("To: rhonel@wx6ju06h.mailosaur.net".encode())
clientSocket.send("From: syed@gmail.com".encode())
clientSocket.send(msg.encode())
	
# Message ends with a single period.
print ("Period")
clientSocket.send(endmsg.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != "354":
    print ("354 reply not received from server.3")
	
# Send QUIT command and get server response.
print ("Quit")
quitCommand = "Quit\r\n"
clientSocket.send(quitCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print (recv8)
if recv8[:3] != "250":
    print ("250 reply not received from server")