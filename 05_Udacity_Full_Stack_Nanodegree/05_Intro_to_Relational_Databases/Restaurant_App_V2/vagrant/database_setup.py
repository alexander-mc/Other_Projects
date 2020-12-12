import sys # the sys module provides a number of functions and variables that can be used to manipulate different parts of the python runtime environment
from sqlalchemy import Column, ForeignKey, Integer, String # import column, fkey, int, and str classes from sql alchemy
from sqlalchemy.ext.declarative import declarative_base # from library, import declarative base to be used in configuration and class code
from sqlalchemy.orm import relationship # import relationship to create foreign key relationships
from sqlalchemy import create_engine # create_engine code will be used in configuration code

Base = declarative_base() # make an instance of the declarative_base class and call it base. The declarative_base will let sql alchemy know that our classes are special sql alchemy classes that correspond to tables in our database

### end of configuration ###


class Restaurant (Base):
	__tablename__ = 'restaurant' # we use the special variable name __tablename__ to let sql alchemy know the variable that we will use to refer to the table
	name = Column(String(80), nullable = False) 
	id = Column(Integer, primary_key = True)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id
		}

class MenuItem(Base):
	__tablename__ = 'menu_item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id')) # create foreign key relationship between menu item class and restaurant class
	restaurant = relationship(Restaurant) # creates a variable to store the relationship of the class Restaurant. Also useful to reference data in the Restaurant class (e.g. print veggieburger.restaurant.name)

# The serialize function below sends JSON objects in a
# serializable format
	@property
	def serialize(self):
		#Returns object data in a serializeable format
		return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }

### insert at end of file ###

engine = create_engine('sqlite:///restaurantmenu.db') # create instance of create_engine class and point to database we will use. The create_engine will CREATE A NEW FILE that we can use similarly to a more robust database like mysql or psql
Base.metadata.create_all(engine) # goes into database and adds the classes we will soon create as new tables in our database
