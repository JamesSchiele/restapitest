import markdown
import os

# Import the framework
from flask import Flask

# Create an insance of Flask
app = Flask(_name_)

@app.route("/")
def index():
    """Present some documentation"""
    
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.txt', 'r') as markdown_file: # open README file from app root

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)