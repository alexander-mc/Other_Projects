# THIS DOES NOT WORK WELL WITH PYTHON 3.6.2; SEE webserver3.py FOR A WORKING FILE.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self): #handles all GET requests our webserver receives
		if self.path.endswith("/restaurants/new"):
#			restaurants = session.query(Restaurant).all()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()

			message = "<html><body>"
			message += "<h1>"
			message += "Make a new restaurant"
			message += "</h>"
			message += "</br></br>"
			message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
			message += "<input name= 'newRestaurantName' type='text' placeholder= 'New Restaurant Name'>"
			message += "<input type= 'submit' value= 'Create'>"
			message += "</body></html>"
			self.wfile.write(message)		
			return

		if self.path.endswith("/edit"):
			restaurant_id = self.path.split("/")[2]
	 		editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	 		if editedRestaurant:
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				message = "<html><body>"
				message += "<h1>"
				message += editedRestaurant.name
				message += "</h1>"
				message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurant_id
				message += "<input name= 'editedRestaurantName' type='text' placeholder= '%s'>" % editedRestaurant.name
				message += "<input type= 'submit' value= 'Rename'>"
				message += "</form>"
				message += "</body></html>"
				self.wfile.write(message)		
				return

		if self.path.endswith("/delete"):
			restaurant_id = self.path.split("/")[2]
	 		deletedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	 		if deletedRestaurant:
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()

				message = "<html><body>"
				message += "<h1>"
				message += "Are you sure you want to delete "				
				message += deletedRestaurant.name
				message += "?"				
				message += "</h1>"
				message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurant_id
				message += "<input type= 'submit' value= 'Delete'>"
				message += "</form>"
				message += "</body></html>"
				self.wfile.write(message)		
				return

		if self.path.endswith("/restaurants"):
			restaurants = session.query(Restaurant).all()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()

			message = "<html><body>"
			message += "<a href = '/restaurants/new'>Make a new restaurant</a>"
			message += "</br></br>"											
			for restaurant in restaurants:
				message += restaurant.name
				message += "</br>"
				message += "<a href ='/restaurants/%s/edit'>Edit</a>" % restaurant.id
				message += "</br>"				
				message += "<a href ='/restaurants/%s/delete'>Delete</a>" % restaurant.id			
				message += "</br></br>"
			message += "</html></body>"
			self.wfile.write(message)		
			return

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
			self.wfile.write(message) #sends a message back to client (write the message to the wfile and then send back to client)
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
			self.wfile.write(message) 
			print (message)
			return

		else:
			self.send_error(404, 'File Not Found %s' % self.path) #notifies you of a 404 or file not found error

	def do_POST(self):
 		try:
 			if self.path.endswith("/restaurants/new"):
 				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type')) 
	 			if ctype == 'multipart/form-data':				
	 				fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('newRestaurantName')

	 			#Create new Restaurant class
	 			newRestaurant = Restaurant(name = messagecontent[0])
	 			session.add(newRestaurant)
	 			session.commit()

	 			#Create a redirect
				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')				
				self.end_headers()

 			if self.path.endswith("/edit"):
 				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type')) 
	 			if ctype == 'multipart/form-data':				
	 				fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('editedRestaurantName')

	 			#Edit restaurant name
				restaurant_id = self.path.split("/")[2]
	 			editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	 			if editedRestaurant:
	 				editedRestaurant.name = messagecontent[0]
	 				session.add(editedRestaurant)
	 				session.commit()

		 			#Create a redirect
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants')				
					self.end_headers()

 			if self.path.endswith("/delete"):

	 			#Delete restaurant name
				restaurant_id = self.path.split("/")[2]
	 			deletedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	 			if deletedRestaurant:
	 				session.delete(deletedRestaurant)
	 				session.commit()

		 			#Create a redirect
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants')				
					self.end_headers()
		except:
			pass

 			"""
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
 			self.wfile.write(message) #send message out to server
 			print (message)
 		except:
 			pass
 			"""

def main(): #code main method
	try:
		port = 8080
		server = HTTPServer(('',port), WebServerHandler) #create server; ('',port) is the server address, which takes the host and port number (leave host as an empty string); webserverHandler is for the 'request handler class' and is defined above 
		print "Webserver running on port %s" % port
		server.serve_forever() # keeps server constantly listening until user calls ctl+c
	except KeyboardInterrupt: # triggered when user holds ctrl+c
		print ("^C entered, stopping web server...")
		server.socket.close() #shut down the server

### run main method when Python interpreter executes script

if __name__ == '__main__':
	main()