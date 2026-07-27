from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
#List all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    return make_response('list workouts', 200)

#Show a single workout with its associated exercises
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    return make_response('show workout', 200)

#Create a Workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    return make_response('create workout', 201)

#Delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    return make_response('delete workout', 204)


if __name__ == '__main__':
    app.run(port=5555, debug=True)