import datetime

from django.db.models import CharField, Model, DateField, TimeField, FloatField


class TrainingPlan(Model):
    date = DateField(default=None)
    description = CharField(max_length=256, default=None)


class Shoe(Model):
    year_of_production = datetime
    shoe_model = CharField(max_length=64)


class RunParameter(Model):
    date = DateField()
    training_plan = CharField(max_length=256, default=None)
    run_name = CharField(max_length=64, default=None)
    distance = FloatField(default=None)
    running_time = CharField(max_length=32)
    paste = CharField(max_length=32)
    pulse_avg = CharField(max_length=32)
    pulse_max = CharField(max_length=32)
    rhythm_avg = CharField(max_length=32)
    step_avg = CharField(max_length=32)
    rise = CharField(max_length=32)
    shoe = CharField(max_length=64)
    comment = CharField(max_length=64, default=None)

