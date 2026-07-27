#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercises
from datetime import date

with app.app_context():

	# reset data and add new example data, committing to db
    #clear tables
    print("Clearing old data...")
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # --- Exercises ---
    print("Seeding exercises...")
    squats = Exercise(name='Back Squat', category='Strength', equipment_needed=True)
    burpees = Exercise(name='Burpees', category='Strength', equipment_needed=False)
    swim = Exercise(name='1.6 Km Swim', category='Cardio', equipment_needed=False)
    plank = Exercise(name='Plank', category='Core', equipment_needed=False)
    cycling = Exercise(name='Cycling', category='Cardio', equipment_needed=True)


    db.session.add_all([squats, burpees, swim, plank, cycling])
    db.session.commit()    

    #WORKOUTS(wo[number]) **letter 'o'**
    print("Seeding workouts...")
    wo1 = Workout(date=date(2025, 1, 10), duration_minutes=60, notes='Leg day')
    wo2 = Workout(date=date(2025, 1, 12), duration_minutes=45, notes='Upper body')
    wo3 = Workout(date=date(2025, 1, 14), duration_minutes=30, notes='Quick cardio')

    db.session.add_all([wo1, wo2, wo3])
    db.session.commit()

    #LINKING WORKOUTS AND EXERCISES
    print("Linking workouts and exercises...")
    we1 = WorkoutExercises(workout_id=wo1.id, exercise_id=squats.id, reps=10, sets=4, duration_seconds=None)
    we2 = WorkoutExercises(workout_id=wo1.id, exercise_id=cycling.id, reps=20, sets=3, duration_seconds=None)
    we3 = WorkoutExercises(workout_id=wo2.id, exercise_id=swim.id, reps=None, sets=None, duration_seconds=1800)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seeding complete successfully!")