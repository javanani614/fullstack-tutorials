from app import db


class Event(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A event has a name, a price and some calories:
    name = db.Column(db.String(50))
    date = db.Column(db.Date)
    starttime = db.Column(db.String(10))
    endtime = db.Column(db.String(10))
    location = db.Column(db.String(100))
    #contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    #contact = db.relationship("contact", backref="events")
    

    def __init__(self, name=None, date=None, starttime=None, endtime=None, location=None):
        self.name = name
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.location = location

    def contact_by_events(self):
        if self.events:
            return self.contact


class Church(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contactname = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(250))
    name = db.Column(db.String(100))
    avatar = db.Column(db.String(250))

    def __init__(self, contactname, password, email, name, avatar):
        self.contactname = contactname
        self.password = password
        self.email = email
        self.name = name
        self.avatar = avatar


def create_event(new_name, new_price, new_calories, new_contact_id):
    # Create a event with the provided input.

    # We need every piece of input to be provided.

    # Can you think of other ways to write this following check?
    if new_name is None or new_price is None or new_calories is None:
        raise Exception("Need name, price and calories!")

    # They can also be empty strings if submitted from a form
    if new_name == '' or new_price == '' or new_calories == '':
        raise Exception("Need name, price and calories!")

    # This line maps to line 16 above (the event.__init__ method)
    event = event(new_name, new_price, new_calories, new_contact_id)

    # Actually add this event to the database
    db.session.add(event)

    # Save all pending changes to the database

    try:
        db.session.commit()
        return event
    except:
        # If something went wrong, explicitly roll back the database
        db.session.rollback()

def get_event_by_contact(contact_id):
    return event.query.filter_by(contact_id=contact_id)

def delete_event(id):

    event = Event.query.get(id)

    if event:
        # We store the name before deleting it, because we can't access it
        # afterwards.
        event_name = event.name
        db.session.delete(event)

        try:
            db.session.commit()
            return "event {} deleted".format(event_name)
        except:
            # If something went wrong, explicitly roll back the database
            db.session.rollback()
            return "Something went wrong"
    else:
        return "event not found"

def list_contacts():
    return contact.query.all()
 
 
def get_contact(id):
    return contact.query.get(id)
 
 
def get_contact_by_contactname(contactname):
    return contact.query.filter_by(contactname=contactname).first()
 
 
def create_contact(contactname, password, email, name, avatar):
    contact = contact(contactname, password, email, name, avatar)
    print str(contact)
    db.session.add(contact)
    db.session.commit()
    return contact
 
 
def update_contact(id, contactname=None, password=None, email=None, name=None,
                avatar=None):
    # This one is harder with the object syntax actually! So we changed the
    # function definition.
 
    contact = contact.query.get(id)
 
    if contactname:
        contact.contactname = contactname
 
    if password:
        contact.password = password

    if email:
        contact.email = email
 
    if name:
        contact.name = name
 
    if avatar:
        contact.avatar = avatar
 
    db.session.commit()
    return contact

import sqlite3

DBFILE = 'contacts.db'  # This defines which file on disc to look in

def connect_to_db():
    """ Get a connection and a cursor. """
    conn = sqlite3.connect(DBFILE)
    db = conn.cursor()
    return (conn, db)


def list_contacts():
    (conn, db) = connect_to_db()
    ### Get all the contacts from the database
    conn.close()
    ### Return the list of contacts


def get_contact(id):
    (conn, db) = connect_to_db()
    ### Get the contact matching the supplied ID
    conn.close()
    ### Return the contact


def get_contact_by_fullname(fullname):
    (conn, db) = connect_to_db()
    ### Get the contact matching the supplied contactname
    conn.close()
    ### Return the contact

def get_contact_by_lastname(lastname):
    (conn, db) = connect_to_db()
    ### Get the contact matching the supplied contactname
    conn.close()
    ### Return the contact

def get_contact_by_firstname(lastname):
    (conn, db) = connect_to_db()
    ### Get the contact matching the supplied contactname
    conn.close()
    ### Return the contact


def create_contact(lastname, firstname, fullname, homephone, cellphone, email, ,church, last_update_ts):
    (conn, db) = connect_to_db()
    ### Use the function arguments - contactname, etc - to INSERT a new contact
    conn.close()
    return 'success'


def update_contact(id, attribute, new_value):
    (conn, db) = connect_to_db()
    ### Update contact by setting attribute to new_value
    conn.close()
    return 'success'

