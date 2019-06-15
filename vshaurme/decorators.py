from functools import wraps

from flask import Markup, flash, url_for, redirect, abort
from flask_login import current_user
from flask_babel import lazy_gettext as _l


def confirm_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            message_template = """{}\n{}\n
                                  <a class="alert-link" href="{}">{}</a>""".format(
                                    _l('Please confirm your account first.'),
                                    _l('Not receive the email?'),
                                    url_for('auth.resend_confirm_email'),
                                    _l('Resend Confirm Email')
                                  )
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

def moderator_required(func):
    return permission_required('MODERATE')(func)
