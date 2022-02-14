from flask import Flask
# Uppercase flask is a class, that has attributes
app = Flask(__name__)
from flask import render_template
# When do you show us index.html? When we call index.html with a backslash
# THis is called a deocrator in Python because it goes right over a function
@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)
# this lets you run a python script as a program
if __name__ == '__main__':
    # Fire up the Flask test server
    # debug my things for me
    # make sure my changes show on the webpage; reload it as I make changes
    app.run(debug=True, use_reloader=True)
