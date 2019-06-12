from functools import wraps

from flask import Markup, flash, url_for, redirect, abort
from flask_login import current_user
from flask_babel import lazy_gettext


def confirm_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            message_template = """{}\n{}\n
                                  <a class="alert-link" href="{}">{}</a>""".format(
                                    lazy_gettext('Please confirm your account first.'),
                                    lazy_gettext('Not receive the email?'),
                                    url_for('auth.resend_confirm_email'),
                                    lazy_gettext('Resend Confirm Email')
                                  )
            # message = Markup(
            #     'Please confirm your account first.'
            #     'Not receive the email?'
            #     '<a class="alert-link" href="%s">Resend Confirm Email</a>' %
            #     url_for('auth.resend_confirm_email'))
            message = Markup(message_template)
            flash(message, 'warning')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return decorated_function


def permission_required(permission_name):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission_name):
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    return permission_required('ADMINISTER')(func)
