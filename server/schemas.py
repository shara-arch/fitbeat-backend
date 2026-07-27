from marshmallow import Schema, fields, validate, ValidationError, post_load
from models import Workout, Exercise, WorkoutExercises


class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    category = fields.String(required=True)
    equipment_needed = fields.Boolean(load_default=False)


class WorkoutSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True)
    notes = fields.String(allow_none=True)


class WorkoutExercisesSchema(Schema):
    id = fields.Integer(dump_only=True)
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
    reps = fields.Integer(allow_none=True)
    sets = fields.Integer(allow_none=True)
    duration_seconds = fields.Integer(allow_none=True)