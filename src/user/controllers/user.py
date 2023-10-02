from flask import Flask, request, jsonify
from services.user import UserService

app = Flask(__name__)
user_service = UserService('mydb', 'myuser', 'mypassword', 'localhost', 5432)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = user_service.create_user(data['username'], data['email'])
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

# Implement routes for update and delete as well
