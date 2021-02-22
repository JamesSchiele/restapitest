import os
import tempfile

import pytest, flask
import datetime as date

from flaskr import flaskr, request, jsonify
from dateutil.relativedelta import relativedelta



app = flask.Flask(_name_)

@pytest.fixture # called by each individual test - simple interface for app to trigger test reqs
def client():
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp() # return low-level file handle and random file name - latter for db name
    flaskr.app.config['TESTING'] = True # disable error catching during request handling for cleaner error reports when testing app

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            flaskr.init_db()
        yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])

def test_empty_db(client): # "test" prefix indicates pytest module to run this as a test
    """ Start with blank db """

    rv = client.get('/')
    assert b'No team members here yet' in rv.data

@app.route('/api/team/<string:name>')
def test_correct_age_input(): # test age inputted by post request of user by checking years difference between birthday and today
    rv = client.get('/')
    
    json_data = request.get_json()
    name = json_data['name']
    birthday = json_data['birthday']
    age = json_data['age']

    date_object = datetime.strptime(birthday, "%d-%m-%y")

    difference_in_years = relativedelta(date.today(), start_date).years

    if (difference_in_years != age):
        assert b'Invalid age inputted' in rv.data