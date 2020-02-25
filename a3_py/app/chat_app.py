# main app that routes the user to the appropriate web page and allows certain functionality on each page.
# the user can create chat rooms and enter them to send messages

from flask import Flask
from flask import render_template, redirect, flash, url_for
from chatroom import ChatForm
from index import CreateRoomForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


log = dict()  # Server wide chat log for each room, where key = room_name, value = list of messages


def get_room_msgs(dic, name):
    """
    Get all the messages of a certain room
    :param dic: dictionary holding all the message history
    :param name: name of the chat room you want to get the messages out of
    :return: the list of messages from dic[name]
    """
    if name not in dic: # if the key isn't in the dictionary, create it
        dic[name] = list()
    return dic[name]


def add_msg_to_room(dic, name, msg):
    """
    append a new message to a room's list
    :param dic: dictionary holding all the message history on the server
    :param name: name of the chat room
    :param msg: new message
    :return: None
    """
    if name not in dic:
        dic[name] = list()
    dic[name].append(msg)


@app.route('/')
def root():
    """
    If the user doesn't specify an endpoint, redirect them to the index
    :return: a redirect to index
    """
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    web page that allows the user to create an new chat room and also join any of the already created rooms
    :return: a HTML rendering of the web page
    """
    form = CreateRoomForm()  # flask form that allows the user to name create a chat room
    if form.room_name.data in form.rooms:  # disallow two rooms having the same name
        flash("already exists")
    else:
        if form.room_name.data not in ("", None):
            form.rooms.append(form.room_name.data)
    return render_template('index.html', title='Home', form=form)


@app.route('/chatroom/<name>', methods=['GET', 'POST'])
def chatroom(name):
    """
    any web page under the path /chatroom/ will have the same formatting. Allows the user to send a message to the
    server
    :param name: name of the already created chat room
    :return: HTML rendering of the page
    """
    form = ChatForm()  # flask form that takes in user messages

    if form.message.data not in ("", None):  # disallow empty messages
        add_msg_to_room(log, name, form.message.data)
        redirect('/chatroom/<name>')
    out = get_room_msgs(log, name)

    return render_template('chatroom.html', title='Chatroom: ' + name, form=form, name=name, out=out)


# EOF
