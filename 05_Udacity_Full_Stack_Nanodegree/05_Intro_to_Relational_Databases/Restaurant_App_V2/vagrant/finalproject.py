# See file 'project2.py', which includes NOTES about this code! #

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# API endpoints via JSON

@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(MenuItem = menuItem.serialize)

@app.route('/restaurants/JSON/')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])


# Routes

# Restaurant Main Page

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
	restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
	return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurants/new/', methods=['GET','POST'])
def newRestaurant():
	if request.method == 'POST':
		newRestaurant = Restaurant(name= request.form['name'])
		session.add(newRestaurant)
		session.commit()
		flash("New restaurant created!")
		return redirect(url_for('showRestaurants'))
	else:
		return render_template('newRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash("Restaurant name changed!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant_id = restaurant_id, editedRestaurant = editedRestaurant)

@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
	restauranttodelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		session.delete(restauranttodelete)
		session.commit()
		flash("Restaurant deleted.")
		return redirect(url_for('showRestaurants'))
	else:
		return render_template('deleteRestaurant.html', restaurant_id = restaurant_id, restauranttodelete = restauranttodelete)

# Restaurant Menu Pages

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
	num_appetizers = 0
	num_entrees = 0
	num_beverages = 0 
	num_desserts = 0
	num_beverages = 0
	num_extras = 0
	for i in items:
		if i.course == 'Appetizer':
			num_appetizers += 1
		elif i.course == 'Entree':
			num_entrees += 1
		elif i.course == 'Beverage':
			num_beverages += 1
		elif i.course == 'Dessert':
			num_desserts += 1
		else:
			num_extras += 1
	return render_template('menu.html', restaurant=restaurant, items=items, num_appetizers=num_appetizers, num_entrees=num_entrees, num_beverages=num_beverages, num_desserts=num_desserts, num_extras=num_extras)

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newItem = MenuItem(name= request.form['name'], description= request.form['description'], price= request.form['price'],course= request.form['course'], restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		flash("New menu item created!")
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newMenuItem.html', restaurant_id = restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:            
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash("Successfully edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html', menu_id = menu_id, item = editedItem)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemtodelete = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(itemtodelete)
		session.commit()
		flash("Item deleted.")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('deleteMenuItem.html', item = itemtodelete)

# Access server from Terminal

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.debug = True
	app.run(host = '0.0.0.0', port=8000)