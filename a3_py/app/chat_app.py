from flask import Flask
from flask import render_template, redirect, flash
from chatroom import ChatForm
from index import CreateRoomForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a'


chat_logs = dict()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = CreateRoomForm()
    flash("test flash")
    if form.room_name.data in form.rooms:
        flash("already exists")
    else:
        if form.room_name.data not in ("", None):
            form.rooms.append(form.room_name.data)
    print(form.rooms)
    return render_template('index.html', title='Home', form=form)


@app.route('/chatroom/<name>', methods=['GET', 'POST'])
def chatroom(name):
    form = ChatForm()

    if form.message.data not in ("", None):
        form.all_messages.append(form.message.data)
    redirect('/chatroom/<name>')

    chat_logs[name] = form.all_messages

    print(chat_logs[name])
    return render_template('chatroom.html', title='Chatroom: ' + name, form=form, name=name, chat=chat_logs)




# EOF
