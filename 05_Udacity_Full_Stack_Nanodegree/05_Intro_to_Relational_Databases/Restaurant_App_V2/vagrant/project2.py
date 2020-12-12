from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# ^ import flask class from Flask library
# with flask, we don't have to write out response codes!

app = Flask(__name__)
# ^ create instance of the class with the name of the running application as an argument
# anytime we run an application in Python, a special variable called name
# gets defined for the application and all of the imports it uses

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Connect to Database and create database session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Make an API Endpoint (GET Request) to get a collection of restaurant menu items
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(MenuItem = menuItem.serialize)

@app.route('/')
def DefaultRestaurantMenu():
# ^ this is a 'decorator' = It wraps our function inside the app.route
# function that Flask has already created. If any of these routes get
# sent from the browser, the function that we define gets executed
# since this is stacked on top of the below code, the @app.route('/')
# function will call the @app.route('/hello') function
	restaurant = session.query(Restaurant).first()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	output = ''
	for i in items:
		output += i.name
		output += '</br>'
		output += i.price
		output += '</br>'
		output += i.description
		output += '</br>'
		output += '</br>'
		
	return output

@app.route('/restaurant/<int:restaurant_id>/')
# ^ so if either route localhost:8000/ or localhost:8000/hello is visited,
# the below function gets invoked
def restaurantMenu(restaurant_id):

	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
	
	return render_template('menu.html', restaurant=restaurant, items=items)
""" Replace below code with render template code (above)
	output  = ''
	for i in items:
		output += i.name
		output += '</br>'
		output += i.price
		output += '</br>'
		output += i.description
		output += '</br>'
		output +='</br>'
	return output
"""	


#Functions

#Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		# ^ Looks for a POST request.
		newItem = MenuItem(name= request.form['name'], restaurant_id = restaurant_id)
		# ^ The requst method pulls from the form calling the function (newMenuItem.html)
		session.add(newItem)
		session.commit()
		flash("New menu item created!")
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newMenuItem.html', restaurant_id = restaurant_id)

#Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("Successfully edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('editmenuitem.html', menu_id = menu_id, item = editedItem)

#Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemtodelete = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(itemtodelete)
		session.commit()
		flash("Item deleted.")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('deleteMenuItem.html', item = itemtodelete)






if __name__ == '__main__':
# ^ The application run by the PYTHON INTERPRETER gets a name variable
# set to __main__, whereas all the other imported Python files get 
# __name__ variable set to the actual name of the python
# The if statement makes sure the server ONLY runs if the script is
# executed directly from the PYTHON INTERPRETER, NOT used as an imported
# module. However, if imported, you still have access to the rest of
# the code.
# By default, the server is only accessible from the host machine
# and not from any other computer. However, since we're using a vagrant environment,
# we must make our server publicly available by changing the call of the
# run method to look like below, with the host and port arguments.
	app.secret_key = 'super secret key'
	# Flask uses this to create sessions for users (normally this would be a secure password if application was live on internet)
	app.debug = True
	# ^ Setting this to true enables flask to reload the server whenver there is a change in code
	# so you don't have to do so every time you make a change.
	# It also provides a helpful debugger in the browser if things go wrong.
	app.run(host = '0.0.0.0', port=8000)
	# ^ the run function runs the local server with our application
	# 0.0.0.0 tells the server to look on all public IP addresses