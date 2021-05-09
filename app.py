from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home_page():
    """Show Home Page"""
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    """Show form to add a new pet for adoption"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80'
        if form.photo_url.data != '':
            photo_url = form.photo_url.data 
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f'{name} added to adoption list')

        return redirect('/')
    else:    
        return render_template('add_pet_form.html',form=form)

@app.route('/<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    """Edit existing pet"""
    pet = Pet.query.get(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        
        db.session.add(pet)
        db.session.commit()
        flash(f'{pet.name} edited on the adoption list')

        return redirect('/')
    else:    
        return render_template('edit_pet_form.html',form=form, pet=pet)