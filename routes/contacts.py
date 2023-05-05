from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))

#Cuando le da al boton guardar pasa a ejecutar el metodo post
@contacts.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # Obtiene la data ingresada en la pagina con los datos que solicita
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    #se borra el contacto
    db.session.delete(contact)
    #manda un commit a la base de datos con los datos actualizados
    db.session.commit()

    flash('Contact deleted successfully!')
    #redirige al contacto,index
    return redirect(url_for('contacts.index'))


@contacts.route("/about")
def about():
    return render_template("about.html")
