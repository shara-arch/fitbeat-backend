from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
# 1. Exercise Model
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    # relationships 
    # An Exercise have many WorkoutExercises
    workout_exercises = db.relationship(
        'WorkoutExercises',
        back_populates='exercise',
        cascade='all, delete-orphan'
    )
    # An Exercise has many Workouts through WorkoutExercises
    workouts = db.relationship(
        'Workout',
        secondary='workout_exercises',
        viewonly=True
    )
    #Table constraints(to ensure no exercises share names)
    __table_args__ = (
        db.UniqueConstraint('name', name='uq_exercise_name'),
    )
    # ... columns ... 



# 2.Workout Model    
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # relationships 
    # A Workout has many WorkoutExercises
    workout_exercises = db.relationship(
        'WorkoutExercises',
        back_populates='workout',
        cascade='all, delete-orphan'
    )
    #A Workout has many exercises through WorkoutExercisses
    exercises = db.relationship(
        'Exercise',
        secondary='workout_exercises',
        viewonly=True
    )    
    # Model Validation(Ensures the duration of each exercise exceedes 0min)
   

# 3. WorkoutExercises joined Model
class WorkoutExercises(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # relationships 
    # WorkoutExercises belong to Workout and Exercise
    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    #Validation
