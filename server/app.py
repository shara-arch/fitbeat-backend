from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from marshmallow import ValidationError 

from models import db, Workout, Exercise, WorkoutExercises


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
#List all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    schema = WorkoutSchema(many=True)
    return make_response(schema.dump(workouts), 200)

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

#List an Exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    return make_response('list exercises', 200)

#Show an exercise and associated workouts
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    return make_response('show exercise', 200)

#Create an exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    return make_response('create exercise', 201)

#Delete an exercise
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return make_response('delete exercise', 204)

#Add an exercise to a workout, including reps/sets/duration
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return make_response('add exercise to workout', 201)

if __name__ == '__main__':
    app.run(port=5555, debug=True)