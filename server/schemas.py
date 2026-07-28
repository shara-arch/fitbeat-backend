from marshmallow import Schema, fields, validate, ValidationError, post_load, validates_schema
from models import Workout, Exercise, WorkoutExercises


class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    # Model: nullable=False, uq_exercise_name
    name = fields.String(
        required=True, 
        validate=[validate.Length(min=1, error="Name cannot be empty.")]
    )
    # Model: nullable=False
    category = fields.String(
        required=True, 
        validate=[validate.Length(min=1, error="Category cannot be empty.")]
    )
    equipment_needed = fields.Boolean(load_default=False)


class WorkoutSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date(required=True)
    
    # Model: CheckConstraint('duration_minutes > 0') and @validates('duration_minutes')
    duration_minutes = fields.Integer(
        required=True, 
        validate=validate.Range(min=1, error="Workout duration MUST be more than 0 minutes.")
    )
    notes = fields.String(allow_none=True)


class WorkoutExercisesSchema(Schema):
    id = fields.Integer(dump_only=True)
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
    
    # Model: @validates('reps', 'sets', 'duration_seconds') -> must be non-negative (>= 0)
    reps = fields.Integer(
        allow_none=True, 
        validate=validate.Range(min=0, error="reps must be POSITIVE(>=0)")
    )
    sets = fields.Integer(
        allow_none=True, 
        validate=validate.Range(min=0, error="sets must be POSITIVE(>=0)")
    )
    duration_seconds = fields.Integer(
        allow_none=True, 
        validate=validate.Range(min=0, error="duration_seconds must be POSITIVE(>=0)")
    )

    # Model rule: Ensures at least one of reps, sets, or duration_seconds is provided
    @validates_schema
    def validate_at_least_one_metric(self, data, **kwargs):
        reps = data.get('reps')
        sets = data.get('sets')
        duration_seconds = data.get('duration_seconds')

        if reps is None and sets is None and duration_seconds is None:
            raise ValidationError(
                "At least one of 'reps', 'sets', or 'duration_seconds' must be provided."
            )


# Nested Schemas for displaying relationships
class ExerciseWithWorkoutsSchema(ExerciseSchema):
    workouts = fields.List(fields.Nested(WorkoutSchema))


class WorkoutWithExercisesSchema(WorkoutSchema):
    exercises = fields.List(fields.Nested(ExerciseSchema))
    workout_exercises = fields.List(fields.Nested(WorkoutExercisesSchema))

    