import os
import random

from PIL import Image
from faker import Faker
from flask import current_app
from sqlalchemy.exc import IntegrityError

from vshaurme.extensions import db
from vshaurme.models import User, Photo, Tag, Comment, Notification

fake = Faker("ru_RU")


def fake_admin():
    admin = User(name=fake.name(),
                 username=fake.user_name(),
                 email="{}-{}".format('admin',fake.email()),
                 bio=fake.sentence(),
                 website=fake.uri(),
                 confirmed=True)
    admin.set_password('helloflask')
    notification = Notification(message='Hello, welcome to Vshaurme.', receiver=admin)
    db.session.add(notification)
    db.session.add(admin)
    db.session.commit()


def fake_user(count=10):
    for user_number in range(count):
        user = User(name=fake.name(),
                    confirmed=True,
                    username=fake.user_name(),
                    bio=fake.sentence(),
                    location=fake.city(),
                    website=fake.uri(),
                  )
        user.set_password('123456')
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_follow(count=30):
    for _ in range(count):
        user = User.query.get(random.randint(1, User.query.count()))
        user.follow(User.query.get(random.randint(1, User.query.count())))
    db.session.commit()


def fake_tag(count=20):
    for tag_number in range(count):
        tag = Tag(name=fake.word())
        db.session.add(tag)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_photo(count=30):
    # photos
    upload_path = current_app.config['VSHAURME_UPLOAD_PATH']
    colors = ["#ff80ed",
          "#065535",
          "#133337",
          "#000000",
          "#ffc0cb",
          "#ffffff",
          "#ffe4e1",
          "#008080",
          "#ff0000",
          "#ffd700",
          "#40e0d0",
          "#00ffff",
          "#e6e6fa",
          "#ff7373",
          "#666666",
          "#d3ffce",
          "#ffa500",
          "#f0f8ff",
          "#0000ff",
          "#b0e0e6",
          "#c6e2ff",
          "#faebd7",
          "#7fffd4",
          "#fa8072",
          "#eeeeee",
          "#cccccc",
          "#003366",
          "#800000",
          "#ffb6c1",
          "#800080"]
    for photo_number in range(count):
        filename = 'random_%d.jpg' % photo_number
        file_path = os.path.join(upload_path, filename)
        img = Image.new("RGB", (240, 240), random.choice(colors))
        img.save(file_path)
        # img_small, img_large = 
        photo = Photo(
            description=fake.text(),
            filename=filename,
            filename_m=filename,
            filename_s=filename,
            author=User.query.get(random.randint(1, User.query.count())),
            timestamp=fake.date_time_this_year()
        )

        # tags
        for j in range(random.randint(1, 5)):
            tag = Tag.query.get(random.randint(1, Tag.query.count()))
            if tag not in photo.tags:
                photo.tags.append(tag)

        db.session.add(photo)
    db.session.commit()


def fake_collect(count=50):
    for i in range(count):
        user = User.query.get(random.randint(1, User.query.count()))
        user.collect(Photo.query.get(random.randint(1, Photo.query.count())))
    db.session.commit()


def fake_comment(count=100):
    for i in range(count):
        comment = Comment(
            author=User.query.get(random.randint(1, User.query.count())),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            photo=Photo.query.get(random.randint(1, Photo.query.count()))
        )
        db.session.add(comment)
    db.session.commit()
