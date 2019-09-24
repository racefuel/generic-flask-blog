import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )

    output_size = (250, 250)
    res_img = Image.open(form_picture)
    res_img.thumbnail(output_size)
    res_img.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demomail.com", recipients=[user.email]
    )
    # When working with multi-line strings, the lines need to start from the base of the line. Otherwise if they are left indented, those
    # indentations will show up on the message.
    # _external = True is used to get an absolute url rather than a relative url
    msg.body = f"""To reset your password, visit:
{url_for('users.reset_token', token = token, _external = True)}
If you did not make this request, please ignore this email.
And in that case nothing will be changed.
"""
    mail.send(msg)
