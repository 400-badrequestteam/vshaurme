from vshaurme import create_app
from vshaurme.extensions import db

app = create_app()
db.create_all(app=app)

if __name__ == '__main__':
    app.run()
