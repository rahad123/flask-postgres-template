from flask import Flask, render_template, request, redirect, url_for
from src.user.validators import user
# from src.app import app

app = Flask(__name__)
books = []


# For validation
data = {"name": "Red", "age": 28}
person = user.Person(**data)

# # Accessing parsed data
print(person.name)  # Output: "Red"
print(person.age)   # Output: 28

# Validation and error handling
invalid_data = {"name": "Bob", "age": "thirty"}
try:
    # This will raise a validation error
    person = user.Person(**invalid_data)
except ValueError as e:
    print(e)
# person = user.Person(user.walk())

books = [
    {"id": 1, "title": "title-1", "author": "author-1"},
    {"id": 2, "title": "title-2", "author": "author-2"},
    {"id": 3, "title": "title-3", "author": "author-3"},
]


@app.route("/", methods=["GET"])
def getBooks():
    return books


@app.route("/create", methods=["POST"])
def createBooks():
    return books


if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.131")
