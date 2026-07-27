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