import csv
from flask import Flask
# Uppercase flask is a class, that has attributes
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path)
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list
# When do you show us index.html? When we call index.html with a backslash
# THis is called a deocrator in Python because it goes right over a function
@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)
    # first one is what the template knows it byu, second is what the function knows it by
# this lets you run a python script as a program
if __name__ == '__main__':
    # Fire up the Flask test server
    # debug my things for me
    # make sure my changes show on the webpage; reload it as I make changes
    app.run(debug=True, use_reloader=True)
