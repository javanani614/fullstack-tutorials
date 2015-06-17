from app import db

class Route (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_street  = db.Column(db.String(100))
    end_street = db.Column(db.String(100))
    streets = db.Column(db.String(500))
    total_households = db.Column(db.Integer)
    directions = db.Column(db.String(500))
    team_id = db.Column(db.Integer)
    #will also have an event id
   
    def __init__(self, houseno=None, street=None, street2=None, city=None, state=None, zipcode=None):
        self.houseno = houseno
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    houseno  = db.Column(db.Integer)
    street  = db.Column(db.String(100))
    street2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
   
    def __init__(self, houseno=None, street=None, street2=None, city=None, state=None, zipcode=None):
        self.houseno = houseno
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    middle_initial = db.Column(db.String(1))
    homephone = db.Column(db.String(10))
    cellphone = db.Column(db.String(10))
    email = db.Column(db.String(250))
    birthdate = db.Column(db.Date)
    last_update_ts = db.Column(db.String(16))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    #contact = db.relationship("Address", backref="contacts")
    

    def __init__(self, lastname=None, firstname=None, middle_initial=None, homephone=None, cellphone=None, email=None, birthdate=None, route_id=None, last_update_ts=None):
        self.lastname = lastname
        self.firstname = firstname
        self.middle_initial = middle_initial
        self.homephone = homephone
        self.cellphone = cellphone
        self.email = email
        self.birthdate = birthdate
        self.route_id = route_id
        self.last_update_ts = last_update_ts




def list_contacts():
    return Contact.query.all()
 
 
def get_contact(id):
    return Contact.query.get(id)
 
 
#def get_contact_by_name(firstname, lastname):
#    return contact.query.filter_by(firstname=self.firstname && lastname=self.lastname).first()
 
 
def create_contact(lastname, firstname, middle_initial,  cellphone, email):
    print 'adding the following contact' + lastname + firstname + cellphone
    contact = Contact(lastname, firstname, middle_initial, cellphone, email)
    print 'adding the following contact' + lastname + firstname + cellphone
    #print str(contact)
    db.session.add(contact)
    db.session.commit()
    return contact
 
 
def update_contact(id, lastname, firstname, middle_initial, homephone, cellphone, email, birthdate, route_id):
               
    # This one is harder with the object syntax actually! So we changed the
    # function definition.
 
    contact = Contact.query.get(id)
 
    if lastname:
        contact.lasttname = lasttname
 
    if firstname:
        contact.firstname = firstname

    if middle_initial:
        contact.middle_initial = middle_initial

    if email:
        contact.email = email
 
    if homephone:
        contact.homephone = homephone
 
    if cellphone:
        contact.cellphone = cellphone

    if birthdate:
        contact.birthdate = birthdate
 
 
    db.session.commit()
    return contact

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"

