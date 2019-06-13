from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from vshaurme.extensions import mail
from flask import url_for
from flask_babel import lazy_gettext as _l


def send_mail(to, subject, template, **kwargs):
    msg_body = render_template('emails/confirm.html', user=kwargs["user"], token = kwargs["token"])
    msg = Message(subject=subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to],
                  html=msg_body)
    with current_app.app_context():
        mail.send(msg)


def send_confirm_email(user, token, to=None):
    send_mail(subject=_l('Email Confirm'), to=to or user.email, template='emails/confirm', user=user, token=token)


def send_reset_password_email(user, token):
    send_mail(subject=_l('Password Reset'), to=user.email, template='emails/reset_password', user=user, token=token)


def send_change_email_email(user, token, to=None):
    send_mail(subject=_l('Change Email Confirm'), to=to or user.email, template='emails/change_email', user=user, token=token)
