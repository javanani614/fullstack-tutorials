from flask import render_template, request

from contactDAO import  Contact, create_contact

from app import app



@app.route('/')
def index():
     return render_template('contact.html')


@app.route('/signin', methods=['GET', 'POST'])
def createContact():

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.

    lastname = request.form.get('last_name')
    print "last name = " + lastname
    firstname = request.form.get('first_name')
    middle_initial = request.form.get('middle_initial')
    cellphone = request.form.get('cellphone')
    email =request.form.get('email')
    #contact = create_contact(lastname, firstname, middle_initial,  cellphone, email)

    # Now we are checking the input in create_dessert, we need to handle
    # the Exception that might happen here.

    # Wrap the thing we're trying to do in a 'try' block:
    try:
        contact = create_contact(lastname, firstname, middle_initial, cellphone, email)
        if contact == None:
            print "it did not work" 
        return render_template('add.html', lastname = lastname, firstname= firstname, middle_initial=middle_initial,cellphone=cellphone,email=email)
        
    except Exception as e:
        # Oh no, something went wrong!
        # We can access the error message via e.message:
        return render_template('add.html', error=e.message)



@app.route('/delete/<id>')
def delete(id):

    message = delete_contact(id)

    return index()  # Look at the URL bar when you do this. What happens?
