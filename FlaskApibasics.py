#What is Flask
'''Flask is a lightweight Python web framework used to build:
Web applications
REST APIs
Backend services
Microservices
CRUD applications
In simple words:
Flask allows Python code to communicate with clients through HTTP requests and responses.

Frontend / Postman / Browser
          |
          | HTTP Request
          ↓
       Flask API
          |
          ↓
       Python Code
          |
          ↓
       Database
          |
          ↓
      HTTP Response'''

#What is an API
'''
API means Application Programming Interface.
An API allows two different applications to communicate with each other.

For example, suppose you have a frontend application:

React Application
       |
       | GET /users
       ↓
Flask API
       |
       ↓
PostgreSQL

The React application asks:"Give me all users."

Flask receives the request, gets the data from the database, and sends it back.'''


#What is Flask API : A Flask API is an API created using the Flask framework.
'''from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World"
if __name__=="__main__":
      app.run()'''

'''Start server
if __name__ == "__main__":
    app.run(debug=True)
This starts the Flask development server.'''

#What is a Route : A route is a URL path associated with a Python function.
'''Example:
@app.route("/users")
def users():
    return "Users"

Now:http://127.0.0.1:5000/users will return:Users'''

#HTTP Methods in Flask are
'''
GET
POST
PUT
PATCH
DELETE
'''



'''from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Database connection
DATABASE_URL = "postgresql://postgres:Ashu136@localhost:5433/FastAPI"

engine = create_engine(DATABASE_URL)


@app.route("/")
def home():
    return "Flask API is working!"


@app.route("/users", methods=["GET"])
def get_users():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT id, name, email, age FROM users")
        )

        users = []

        for row in result:
            users.append({
                "id": row.id,
                "name": row.name,
                "email": row.email,
                "age": row.age
            })

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
'''



from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = "postgresql://postgres:Ashu136@localhost:5433/FastAPI"

engine = create_engine(DATABASE_URL)


@app.route("/users", methods=["POST"])
def create_user():

    data = request.json

    name = data["name"]
    email = data["email"]
    age = data["age"]

    with engine.connect() as connection:

        connection.execute(
            text("""
                INSERT INTO users (name, email, age)
                VALUES (:name, :email, :age)
            """),
            {
                "name": name,
                "email": email,
                "age": age
            }
        )

        connection.commit()

    return jsonify({
        "message": "User created successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)





















