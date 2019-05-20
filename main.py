from vshaurme import create_app
from vshaurme.extensions import db

app = create_app()

###################################################### rollback initiation begin

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token 
        '68ba7e63b1e947948dfa6e9d983ae623',
        # environment name
        'vshaurme',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    rollbar.report_message('Rollbar is configured correctly')
    
    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

###################################################### rollback initiation end

db.create_all(app=app)

if __name__ == '__main__':
    app.run(debug = False, use_reloader = True)
