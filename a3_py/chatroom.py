from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

class ChatForm(FlaskForm):
    message = StringField("your message")
    send = SubmitField("Send")


