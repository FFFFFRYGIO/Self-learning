from student import StudentDB
import pytest

# setup method executing before any test
@pytest.fixture(scope='module')
def db():
    print('---setup---')
    db = StudentDB()
    db.connect('data.json')
    yield db  # not return, because we want to let the following code execute
    print('---teardown---')
    db.close()

"""
# setup method executing before any test
db=None
def setup_module(module):
    print('---setup---')
    global db
    db = StudentDB()
    db.connect('data.json')

# teardown method after tests are finished
def teardown_module(module):
    print('---teardown---')
    db.close()
"""

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'