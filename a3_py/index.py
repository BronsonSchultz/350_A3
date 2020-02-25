from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm



class CreateRoomForm(FlaskForm):
    """
    flask form that allows the user to create a chat room
    """
    rooms = list()  # list of all the different chat room names
    room_name = StringField("your message")  # allows the user to enter a name for a new room
    create = SubmitField("Create")  # submit button to send the message that a oom should be created

