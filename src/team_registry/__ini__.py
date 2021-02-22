import markdown
import os
import shelve

# Import the framework
from flask import Flask, g

# Create an insance of Flask
app = Flask(_name_)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("teammates.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    """Present some documentation - README.txt"""
    
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.txt', 'r') as markdown_file: # open README file from app root

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

 # create a class for each endpoint
class TeammateList(Resource):
    def get(self): # get method for getting team mate list
        shelf = get_db()
        members = list(shelf.keys())

        team = [] # array of team members

        for member in members:
            team.append(shelf[member]) # loop over all keys in team member list, put in array and append to team array
        
        return {'message':'Success', 'data': team} # wrap in data field to add message

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required = True)
        parser.add_argument('birthday', required = True)
        parser.add_argument('age', required = True)
        parser.add_argument('favourite_animal', required = True)

        # Parse arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['name']] = args # expected to be unique keys

        return {'message': 'Team member added', 'data':args }, 201

class TeamMember(Resource):
    def get(self, name):
        # receive 'name' as part of URL function here and pass through as a parameter
        shelf = get_db()

        # Return 404 error if key (name) does not exist in team members.
        if not (name in shelf):
            return {'message': 'Team member not found', 'data':{}}, 404

        # If team member exists, return information

        return {'message':'Team member exists in db', 'data': shelf[name]}, 200
    
api.add_resource(TeammateList, '/team')
api.add_resource(TeamMember, '/team/<string:name>')
