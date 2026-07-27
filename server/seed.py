#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercises
from datetime import date

with app.app_context():

	# reset data and add new example data, committing to db
    #clear tables
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # --- Exercises ---
    squats = Exercise(name='Back Squat', category='Strength', equipment_needed=True)
    burpees = Exercise(name='Burpees', category='Strength', equipment_needed=False)
    swim = Exercise(name='1.6 Km Swim', category='Cardio', equipment_needed=False)
    plank = Exercise(name='Plank', category='Core', equipment_needed=False)
    cycling = Exercise(name='Cycling', category='Cardio', equipment_needed=True)


    db.session.add_all([squats, burpees, swim, plank, cycling])
    db.session.commit()    

    #WORKOUTS(wo[number]) **letter 'o'**
    wo1 = Workout(date=date(2025, 1, 10), duration_minutes=60, notes='Leg day')
    wo2 = Workout(date=date(2025, 1, 12), duration_minutes=45, notes='Upper body')
    wo3 = Workout(date=date(2025, 1, 14), duration_minutes=30, notes='Quick cardio')

    db.session.add_all([wo1, wo2, wo3])
    db.session.commit()