from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from vshaurme.extensions import mail
from flask import url_for

###################################################### rollback initiation begin

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
###################################################### rollback initiation end

def send_mail(to, subject, template, **kwargs):
    msg_body = render_template('emails/confirm.html', user=kwargs["user"], token = kwargs["token"])
    msg = Message(subject=subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to],
                  html=msg_body)
    
    rollbar.report_message('MAIL_USERNAME=' + current_app.config['MAIL_USERNAME'], 'info')

    '''with current_app.app_context():
        mail.connect()
        mail.send(msg)'''


def send_confirm_email(user, token, to=None):
    send_mail(subject='Email Confirm', to=to or user.email, template='emails/confirm', user=user, token=token)


def send_reset_password_email(user, token):
    send_mail(subject='Password Reset', to=user.email, template='emails/reset_password', user=user, token=token)


def send_change_email_email(user, token, to=None):
    send_mail(subject='Change Email Confirm', to=to or user.email, template='emails/change_email', user=user, token=token)
