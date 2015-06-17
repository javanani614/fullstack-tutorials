import traceback

from contactDAO import db, create_contact, get_contact


def check_test(func):
    """ This is a decorator that simply prints out whether the function
        it calls succeeded or not. You don't need to edit this.
    """
    def func_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print ":) {} passed".format(func.__name__)
        except AssertionError:
            traceback.print_exc()
            print ":( {} failed".format(func.__name__)
    return func_wrapper


# ## Testing validation for creating a new contact.
@check_test
def test_create_contact():
    lastname = "testlast"
    firstname = "testfirst"
    middle_initial = "M"
    cellphone = "7071234567"
    email = "emailforme@yahoo.com"
    contact =  create_contact(lastname, firstname, middle_initial,  cellphone, email)
    assert contact is not None
    #assert len(desserts) > 0

@check_test
def test_get_contact():
    id = 1
    contact = get_contact(id)

    assert contact is not None

    # Delete this contact now we are done
    db.session.delete(contact)
    db.session.commit()



if __name__ == "__main__":

    # Run every method in this file which starts with test_.

    for item in dir():
        # Loop through all the defined items we know about (functions, etc).
        # If the name starts with test_, assume it's a test and run it!
        if item.startswith('test_'):
            globals()[item]()
