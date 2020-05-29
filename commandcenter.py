import flask
import lib.Logger
import lib.Database
import os
from passlib.context import CryptContext
import markupsafe

logger = lib.Logger.Logger(__name__, "debug")
app = flask.Flask(__name__)
password_hasher = CryptContext(schemes='bcrypt')
mongoclient = lib.Database.DatabaseInteraction()

logger.log("info", "flask started")

# Functions #


def get_users():
    userlist = []
    mongoclient.setdatabase('smarthome-db')
    mongoclient.setcollection("People")
    data = mongoclient.getcollection()
    new_users = data.find()
    for item in new_users:
        userlist.append(item['name'])
    return userlist


def add_user(username, password):
    mongoclient.setdatabase('smarthome-db')
    mongoclient.setcollection('People')
    data = {
        'name': username,
        'password': password
    }
    mongoclient.setdocument(data)
    mongoclient.insertdocument()

# Vars #


app.secret_key = os.urandom(32)
navbar = {'Home': '', 'To Do': 'todo', 'Schedule': 'schedule', 'Shopping List': 'shopping',
          'Change User': 'changeuser', "Log Out": 'logout'}
userList = get_users()

# Flask Stuff #


# Templates #
@app.route('/')
def index(nav=navbar):
    if 'username' in flask.session:
        return flask.render_template('index.html', nav=nav, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login(nav=navbar):
    if flask.request.method == 'POST':
        flask.session['username'] = flask.request.form['username']
        if flask.session['username'] in userList:
            return flask.redirect(flask.url_for('index'))
        flask.redirect(flask.url_for('/login/new/<newuser>'))
    return flask.render_template('login.html')


@app.route('/login/new',  methods=['GET', 'POST'])
def newuser(nav=navbar):
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        password = password_hasher.hash(password)
        add_user(username, password)
        flask.session['username'] = username
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('new_user.html')


@app.route('/login/new/<newuser>')
def newuser_name(newuser, nav=navbar):
    return flask.render_template('new_user.html', username=newuser)


@app.route('/login_error')
def login_error():
    return flask.render_template('login_error.html')


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
        userlist = get_users()
        if flask.request.method == 'POST':
            flask.session['username'] = flask.request.form['username']
            return flask.redirect(flask.url_for('index'))
        return flask.render_template('changeuser.html', nav=nav, userlist=userlist, user=flask.session['username'])
    return flask.redirect(flask.url_for('login'))
