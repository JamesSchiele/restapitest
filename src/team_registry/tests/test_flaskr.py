import os
import tempfile

import pytest

from flaskr import flaskr


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

