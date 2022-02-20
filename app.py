import csv
from flask import Flask
from flask import abort
# Uppercase flask is a class, that has attributes
from flask import render_template
app = Flask(__name__)
# a Python convention. evaluates to the name of the current module. Current module here is "app" because app.py.

# make a function
def get_csv():
    # give filepath to variable
    csv_path = './static/la-riots-deaths.csv'
    # pass opening of file to another variable
    csv_file = open(csv_path)
    # read the file, assigned to another variable
    csv_obj = csv.DictReader(csv_file)
    # turn csv into a list. Helps us keep track of it, since csv can only be iterated over once.
    csv_list = list(csv_obj)
    return csv_list
# When do you show us index.html? When we call index.html with a backslash
# THis is called a decorator in Python because it goes right over a function
@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    # call the render template function
    # expects name of  template, and context of template
    return render_template(template, object_list=object_list)
    # first one is what the template will know it as.
@app.route('/<row_id>/')
# row_id is an argument that must exist for "detail" to work
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(418)
if __name__ == '__main__':
    # Fire up the Flask test server
    # debug my things for me
    # make sure my changes show on the webpage; reload it as I make changes
    app.run(debug=True, use_reloader=True)
