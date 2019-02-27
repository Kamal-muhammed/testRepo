# import flask web app class
from flask import Flask, request
import json

# initialize a web app
app = Flask(__name__)

students = [ {"name": "moha", "age": 34, "phone": 77358248278} ]
fruits = ["apple", "orange", "banana"]


# add a url to your web app
@app.route("/")
def hello(): # define a function to do stuff at that route
    return """<h1  style="color:red;">Hello Pykla! Welcome</h1> <br> Flask (A Python Microframework)
flask.pocoo.org>"""

@app.route("/fruits")
def get_all():
	return json.dumps(fruits)

@app.route("/students")
def get_students():
	return str(students)

@app.route("/students/1")
def get_one():
	one =students[0]
	return f"{one['name']} is {str(one['age'])} years old and can be contacted on {one['phone']}"

@app.route('/students', methods=["POST"])
def add_student():
	data = request.get_json()
	students.append(data)
	return str(students)

@app.route("/students/delete/<name>", methods=["DELETE"])
def delete_one(name):
	for std in students:
		if std['name']==name:
			record = std 
	students.remove(record)
	return str(students)



if __name__ == '__main__':
	app.run(debug=True)

