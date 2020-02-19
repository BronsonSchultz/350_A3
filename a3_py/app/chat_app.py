from flask import Flask
from flask import render_template, flash, redirect
from chatroom import ChatForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a'


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bro'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'eyo'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/chatroom/', methods=['GET', 'POST'])
def chatroom():
    form = ChatForm()

    # if form.validate_on_submit():
    print(form.message.data)
    form.all_messages.append(form.message.data)
    #     return redirect('/chatroom/')

    # form.saveText(form.message.data)
    return render_template('chatroom.html', title='chatroom', form=form)




# EOF
