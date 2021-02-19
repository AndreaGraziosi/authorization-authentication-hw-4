from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

#Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = GroceryStoreForm()

    if form.validate_on_submit():
        new_GS = GroceryStore(
            title =form.title.data,
            address = form.address.data
        )
        db.session.add(new_GS)
        db.session.commit()
    
        flash('New Grocery Store was created successfully.')
    # - redirect the user to the store detail page.
        return redirect(url_for('main.store_detail', GroceryStore_id=new_GS.id))
    #Send the form to the template and use it to render the form fields
    return render_template('new_store.html', form =form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = GroceryItemForm()

    if form.validate_on_submit():

        new_i = GroceryItem(
            name = form.name.data,
            price = form.price.data,
            category = form.category.data,
            photo_url =form.photo_url.data,
            store = form.store.data
        )
        db.session.add(new_i)
        db.session.commit()

        flash('New item was created successfully.')
    # - redirect the user to the store detail page.
        return redirect(url_for('main.item_detail', GroceryItem_id=new_i.id))

    #  Send the form to the template and use it to render the form fields
    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    form =GroceryStoreForm(obj=store)

    if form.validate_on_submit():
        new_store = GroceryStore(
            address = form.address.data,
            title = form.title.data
        )
        db.session.add(new_store)
        db.session.commit()
    
        flash('Store details were updated successfully.')
        return redirect(url_for('main.store_detail', store_id=new_store.id))
    #Send the form to the template and use it to render the form fields
    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)

    if form.validate_on_submit():
        new_item = GroceryItem(
             name = form.name.data,
            price = form.price.data,
            category = form.category.data,
            photo_url =form.photo_url.data,
            store = form.store.data
        )
        db.session.add(new_item)
        db.session.commit()
    
        flash('Item details were updated successfully.')
        return redirect(url_for('main.item_detail', item_id=new_item.id))
    #Send the form to the template and use it to render the form fields
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item, form=form)

