from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from marshmallow import ValidationError 

from models import db, Workout, Exercise, WorkoutExercises
from schemas import (
    ExerciseSchema,
    WorkoutSchema,
    WorkoutExercisesSchema,
    ExerciseWithWorkoutsSchema,
    WorkoutWithExercisesSchema,
)

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
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({'error': 'Workout not found'}), 404)
    schema = WorkoutWithExercisesSchema()
    return make_response(schema.dump(workout), 200)

#Create a Workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    try:
        workout = WorkoutSchema().load(data)
    except ValidationError as err:
        return make_response(jsonify({'errors': err.messages}), 400)

    new_workout = Workout(
        date=workout['date'],
        duration_minutes=workout['duration_minutes'],
        notes=workout.get('notes')
    )
    db.session.add(new_workout)
    db.session.commit()

    return make_response(WorkoutSchema().dump(new_workout), 201)

#Delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({'error': 'Workout not found'}), 404)

    # cascade='all, delete-orphan' removes associated WorkoutExercises automatically
    db.session.delete(workout)
    db.session.commit()
    return make_response('', 204)

#List an Exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    schema = ExerciseSchema(many=True)
    return make_response(schema.dump(exercises), 200)


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response(jsonify({'error': 'Exercise not found'}), 404)
    schema = ExerciseWithWorkoutsSchema()
    return make_response(schema.dump(exercise), 200)

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