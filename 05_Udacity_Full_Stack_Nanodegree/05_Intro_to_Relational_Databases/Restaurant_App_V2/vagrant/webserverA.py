# THIS DOES NOT WORK WELL WITH PYTHON 3.6.2; SEE webserver3.py FOR A WORKING FILE.

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self): #handles all GET requests our webserver receives
		if self.path.endswith("/hello"): #path contains the url sent by the client to the server as a string. this line of code says look for the url that ends with /hello
			self.send_response(200) #tell webserver to send this response code to indicate a successful GET request
			self.send_header('Content-type','text/html') #respond via text in html to client
			self.end_headers() #sends a blank line indicating the end of http headers and response
			
			message = ""
			message += "<html><body>"
			message += "Hello!"
			message += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
			<h2>What would you like me to say?</h2><input name='message'type='text'><input type = 'submit' value='submit'></form>"
			message += "</body></html>"
			self.wfile.write(bytes(message, "utf-8")) #sends a message back to client
			print (message) # for debugging -- just so you can see your output string in the terminal
			return #exit if statement

		if self.path.endswith("/hola"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
            
			message = ""
			message += "<html><body>"
			message += "&#161 Hola ! <a href = '/hello' >Back to Hello</a>"
			message += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
			<h2>What would you like me to say?</h2><input name='message'type='text'><input type = 'submit' value='submit'></form>"
			message += "</body></html>"
			self.wfile.write(bytes(message, "utf-8"))
			print (message)
			return

		else:
			self.send_error(404, 'File Not Found %s' % self.path) #notifies you of a 404 or file not found error
 
	def do_POST(self):
 		try:
 			self.send_response(301) #when you recive a post, send a request signaling a successful post
 			self.send_header('Content-type', 'text/html')
 			self.end_headers() #decipher the message sent from the server. do this my using some message from the CGI, common gateawy interface, library in Python (note import cgi at top of file)

 			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
 			if ctype == 'multipart/form-data': #check to see if the above form value is being received
 				fields = cgi.parse_multipart(self.rfile, pdict) #collects all of the fields in a form
 				messagecontent = fields.get('message') #gets out the value of a specific field or set of fields and stores them in an array

 			message = ""
 			message += "<html><body>"
 			message += "<h2> Okay, how about this: </h2>"
 			message += "<h1> %s </h1>" % messagecontent[0]
 			message += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
 			<h2>What would you like me to say?</h2><input name='message'type='text'><input type = 'submit' value='submit'></form>" #includes a post request as well as an input type to allow user to input information
 			message += "</html></body>"
 			self.wfile.write(bytes(message, "utf-8")) #send message out to server
 			print (message)
 		except:
 			pass

def main(): #code main method
	try:
		port = 8000
		server = HTTPServer(('',port), WebServerHandler) #create server; ('',port) is the server address, which takes the host and port number (leave host as an empty string); webserverHandler is for the 'request handler class' and is defined above 
		print ("Webserver running on port %s" % port)
		server.serve_forever() # keeps server constantly listening until user calls ctl+c
	except KeyboardInterrupt: # triggered when user holds ctrl+c
		print ("^C entered, stopping web server...")
		server.socket.close() #shut down the server

### run main method when Python interpreter executes script

if __name__ == '__main__':
	main()