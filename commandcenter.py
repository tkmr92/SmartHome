import flask
import lib.Logger

logger = lib.Logger.Logger(__name__, "debug")
app = flask.Flask(__name__)

logger.log("info", "flask started")
navbar = ['home', 'todo', 'schedule', 'shopping', 'change user']


@app.route('/')
def display_home(nav=navbar):
    return flask.render_template('index.html', nav=nav)


@app.route('/todo')
def display_todo(nav=navbar):
    return flask.render_template('todo.html', nav=nav)


@app.route('/schedule')
def display_schedule(nav=navbar):
    return flask.render_template('schedule.html', nav=nav)


@app.route('/shopping')
def display_shopping(nav=navbar):
    return flask.render_template('shopping.html', nav=nav)


@app.route('/changeuser')
def display_change_user(nav=navbar):
    return flask.render_template('changeuser.html', nav=nav)
