from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import time

class ChatForm(FlaskForm):
    all_messages = list()

    message = StringField("your message", validators=[DataRequired()])
    send = SubmitField("Send")

    def get_time(self):
        return time.asctime()[11:16]
