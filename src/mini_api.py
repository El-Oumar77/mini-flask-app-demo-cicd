
from flask import Flask, request, jsonify

app = Flask(__name__)

fake_database = {}
fake_database['email'] = []

@app.route('/api', methods=['GET'])
def get_message():
    # Define the response object
    # 
    response = {'message': 'Hello, world!'}

    # Return the response as JSON
    return jsonify(response)


@app.route('/api/all_users', methods=['GET'])
def get_all_users():
    # Define the response object
    # 
    response = fake_database

    # Return the response as JSON
    return jsonify(response)


@app.route('/api/add_user', methods=['POST'])
def add_user():
    # Extract user data from the request
    user_data = request.json["email"]

    if user_data in fake_database["email"]:
        return jsonify({'message': 'User already exist'}), 400


    # Add user to the fake database
    fake_database['email'].append(user_data)

    # Return a success message
    return jsonify({'message': 'User added successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
