import flask
import lib.Logger
import lib.Database
import os
from passlib.context import CryptContext
import markupsafe

logger = lib.Logger.Logger(__name__, "debug")  # Initialize logging
app = flask.Flask(__name__)  # Initialize Flask
password_hasher = CryptContext(schemes='bcrypt')  # Initialize passlib
mongo_client = lib.Database.DatabaseInteraction()  # Initialize database interaction

logger.log("info", "flask started")

# Functions #


def get_users():
    """
    Helper function to get a list of users currently in the database.
    Since several different pages in our webapp need to retrieve a list of users, this function will help keep
    them more neat.

    :return: user_list (type: list)

    """
    user_list = []
    mongo_client.setdatabase('smarthome-db')
    mongo_client.setcollection("People")
    data = mongo_client.getcollection()
    new_users = data.find()
    for item in new_users:
        user_list.append(item['name'])
    return user_list


def add_user(username, name, password=None):
    """

    :param name:
    :param username:
    :param password:
    :return: None
    """
    mongo_client.setdatabase('smarthome-db')
    mongo_client.setcollection('People')
    if password is None:
        data = {
            'name': username
        }
        mongo_client.setdocument(data)
        mongo_client.insertdocument()
        return
    data = {
        'username': username,
        'name': name,
        'password': password
    }
    mongo_client.setdocument(data)
    mongo_client.insertdocument()
    return

# Vars #


app.secret_key = os.urandom(32)
navbar = {'Home': '', 'To Do': 'todo', 'Schedule': 'schedule', 'Shopping List': 'shopping',
          'Change User': 'changeuser', 'Log Out' : 'logout'}

# Flask Stuff #


# Templates #
@app.route('/')
def index(nav=navbar):
    if 'username' in flask.session:
        return flask.render_template('index.html', nav=nav, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login(nav=navbar):
    user_list = get_users()
    if flask.request.method == 'POST':
        user = flask.request.form['username'].lower()
        password = flask.request.form['password']
        # See if our user is already in our database
        if user in user_list:
            mongo_client.setdatabase('smarthome-db')
            mongo_client.setcollection('People')
            doc = mongo_client.getdocument({'name': user})
            hashed_pass = doc['password']
            # Verify the user input the correct password
            if password_hasher.verify(password, hashed_pass):
                flask.session['username'] = doc['name']
                return flask.redirect(flask.url_for('index'))
            return flask.redirect(flask.url_for('login_error', error='invalid_password'))
        return flask.redirect(flask.url_for('login_error', error='invalid_user'))
    return flask.render_template('login.html')


@app.route('/login/new',  methods=['GET', 'POST'])
def newuser(nav=navbar):
    if flask.request.method == 'POST':
        user_list = get_users()
        username = flask.request.form['username'].lower()
        if username in user_list:
            return flask.redirect(flask.url_for('login_error', error='user_exists'))
        name = flask.request.form['username']
        password = flask.request.form['password']
        password = password_hasher.hash(password)
        add_user(username, name, password)
        flask.session['username'] = name
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('new_user.html')


@app.route('/login/error/<error>')
def login_error(error):
    return flask.render_template('login_error.html', error=error)


@app.route('/logout')
def logout():
    flask.session.pop('username', None)
    return flask.redirect(flask.url_for('login'))


@app.route('/todo')
def todo(nav=navbar):
    if 'username' in flask.session:
        return flask.render_template('todo.html', nav=nav, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))


@app.route('/schedule')
def schedule(nav=navbar):
    if 'username' in flask.session:
        return flask.render_template('schedule.html', nav=nav, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))


@app.route('/shopping')
def shopping(nav=navbar):
    if 'username' in flask.session:
        return flask.render_template('shopping.html', nav=nav, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))


@app.route('/changeuser', methods=['GET', 'POST'])
def change_user(nav=navbar):
    if 'username' in flask.session:
        user_list = get_users()
        if flask.request.method == 'POST':
            flask.session['username'] = flask.request.form['username']
            return flask.redirect(flask.url_for('index'))
        return flask.render_template('changeuser.html', nav=nav, user_list=user_list, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))
