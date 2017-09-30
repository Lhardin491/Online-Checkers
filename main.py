from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    with app.open_resource('recourses/HTML') as f:
        index = f.read()
        return index

with app.test_request_context():
    url_for('static', filename='checkers.css')
