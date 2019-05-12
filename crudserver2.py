#!/usr/bin/env python3

from flask import (Flask, flash, jsonify, redirect,
                   render_template, request, url_for)

app = Flask(__name__)

# Add CRUD functionality
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Make a fake "database" for testing purposes
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
#
# restaurants = [
#     {'name': 'The CRUDdy Crab', 'id': '1'},
#     {'name': 'Blue Burgers', 'id': '2'},
#     {'name': 'Taco Hut', 'id': '3'},
# ]

# Fake menu items
# items = [
#     {'name': 'Cheese Pizza',
#      'description': 'made with fresh cheese',
#      'price': '$5.99',
#      'course': 'Entree',
#      'id': '1'},
#     {'name': 'Chocolate Cake',
#      'description': 'made with Dutch Chocolate',
#      'price': '$3.99',
#      'course': 'Dessert',
#      'id': '2'},
#     {'name': 'Caesar Salad',
#      'description': 'with fresh organic vegetables',
#      'price': '$5.99',
#      'course': 'Entree',
#      'id': '3'},
#     {'name': 'Iced Tea',
#      'description': 'with lemon',
#      'price': '$.99',
#      'course': 'Beverage',
#      'id': '4'},
#     {'name': 'Spinach Dip',
#      'description': 'creamy dip with fresh spinach',
#      'price': '$1.99',
#      'course': 'Appetizer',
#      'id': '5'}
# ]
#
# item = {'name': 'Cheese Pizza',
#         'description': 'made with fresh cheese',
#         'price': '$5.99',
#         'course': 'Entree'}

# JSON API ENDPOINTS (RESTful)
@app.route('/restaurants/JSON')
def restaurantsJSON():
    '''
        Displays list of restaurants in JSON format
    '''
    restaurants = session.query(Restaurant).all()

    return jsonify(Restaurants=[r.serialize for r in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    '''
        Displays a restaurant menu in JSON format
    '''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()

    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    '''
        Displays MenuItem information in JSON format
    '''
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()

    return jsonify(MenuItem=menuItem.serialize)

# Homepage, show all restaurants
@app.route('/')
# best to include trailing '/', it will still load if user forgets it
@app.route('/restaurants/')
def showRestaurants():
    '''
        Displays restaurants on the homepage
    '''
    restaurants = session.query(Restaurant).all()
    # return "This page will show all my restaurants"
    return render_template('restaurants.html', restaurants=restaurants)


# Create new Restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    '''
        Add new Restaurant to database
    '''
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()

        flash("Restaurant successfully created")

        return redirect(url_for('showRestaurants'))
    else:
        # return "This page will be for making a new restaurant"
        return render_template('newRestaurant.html')


# Edit Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    '''
        Edit Restaurant in the database
    '''
    editedRestaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()

        flash("Restaurant successfully edited")

        return redirect(url_for('showRestaurants'))
    else:
        # return "This page will be for editing restaurant %s" % restaurant_id
        return render_template('editRestaurant.html',
                               restaurant_id=restaurant_id,
                               i=editedRestaurant)


# Delete Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    '''
        Delete Restaurant from the database
    '''
    deleteRestaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    if request.method == 'POST':
        session.delete(deleteRestaurant)
        session.commit()

        flash("Restaurant successfully deleted")

        return redirect(url_for('showRestaurants'))
    else:
        # return "This page will be for deleting restaurant %s" % restaurant_id
        return render_template('deleteRestaurant.html', i=deleteRestaurant)


# Show Restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    '''
        Display MenuItem objects (by name, description, price)
    '''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    # return "This page is the menu for restaurant %s" % restaurant_id
    return render_template('menu.html', restaurant=restaurant, items=items,
                           restaurant_id=restaurant_id)


# Create new MenuItem
@app.route('/restaurant/<int:restaurant_id>/menu/new/',
           methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    '''
        Add new MenuItem to database
    '''
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           course=request.form['course'],
                           description=request.form['description'],
                           price=request.form['price'],
                           restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()

        flash("Menu item successfully created")

        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        # return ("This page is for making a new menu item for restaurant %s"
        #         % restaurant_id)
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)

# Edit MenuItem
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    '''
        Edit MenuItem in the database
    '''
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()

    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['course']:
            editedItem.course = request.form['course']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()

        flash("Menu item successfully edited")

        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        # return "This page is for editing menu item %s" % menu_id
        return render_template('editMenuItem.html',
                               restaurant_id=restaurant_id,
                               menu_id=menu_id,
                               item=editedItem)


# Delete MenuItem
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    '''
        Delete a MenuItem from the database
    '''
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()

    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()

        flash("Menu item successfully deleted")

        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        # return "This page is for deleting menu item %s" % menu_id
        return render_template('deleteMenuItem.html', item=deleteItem)


if __name__ == '__main__':
    # Necessary for displaying flashes
    app.secret_key = 'super_secret-key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
