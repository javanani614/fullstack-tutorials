import sqlite3

DBFILE = 'users.db'  # This defines which file on disc to look in

def connect_to_db():
    """ Get a connection and a cursor. """
    conn = sqlite3.connect(DBFILE)
    db = conn.cursor()
    return (conn, db)


def list_users():
    (conn, db) = connect_to_db()
    ### Get all the users from the database
    conn.close()
    ### Return the list of users


def get_user(id):
    (conn, db) = connect_to_db()
    ### Get the user matching the supplied ID
    conn.close()
    ### Return the user


def get_user_by_username(username):
    (conn, db) = connect_to_db()
    ### Get the user matching the supplied username
    conn.close()
    ### Return the user


def create_user(username, email, password, realname, avatar):
    (conn, db) = connect_to_db()
    ### Use the function arguments - username, etc - to INSERT a new user
    conn.close()
    return 'success'


def update_user(id, attribute, new_value):
    (conn, db) = connect_to_db()
    ### Update user by setting attribute to new_value
    conn.close()
    return 'success'