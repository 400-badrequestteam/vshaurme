from flask import url_for

from vshaurme.extensions import db
from vshaurme.models import Notification
from flask_babel import lazy_gettext as _l


def push_follow_notification(follower, receiver):
    message = '{} <a href="{}">{}</a> {}.'.format(_l('User'), 
                                                 url_for('user.index', username=follower.username),
                                                 follower.username,
                                                 _l('followed you')
                                                 )
    notification = Notification(message=message, receiver=receiver)


def push_comment_notification(photo_id, receiver, page=1):
    message = '<a href="{}#comments">{}</a> {}.'.format(
        url_for('main.show_photo', photo_id=photo_id, page=page),
        _l('This photo'),
        _l('has new comment/reply.')
        )
    notification = Notification(message=message, receiver=receiver)


def push_collect_notification(collector, photo_id, receiver):
    message = '{} <a href="{}">{}</a> {} <a href="{}">{}</a>'.format(
        _l('User'),
        url_for('user.index', username=collector.username),
        collector.username,
        _l('collected your'),
        url_for('main.show_photo', photo_id=photo_id),
        _l('photo')
        )                                                                    
    notification = Notification(message=message, receiver=receiver)
