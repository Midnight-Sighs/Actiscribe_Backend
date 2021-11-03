from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
from django.db.models.fields import DateField


class Resident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_first_name = models.TextField(max_length=20)
    r_last_name = models.TextField(max_length=20)
    r_other_identifier = models.TextField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    last_assessment = models.DateField()

class Note(models.Model):
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)
    note_date = models.DateField()
    content = models.TextField(max_length=400)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    dow_one = models.TextField(max_length=20)
    dow_two = models.TextField(max_length=20, blank=True)
    dow_three = models.TextField(max_length=20, blank=True)

class Participation(models.Model):
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)
    date = models.DateField()

class Assessment(models.Model):
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)
    nickname = models.TextField(max_length=20, blank=True)
    games_yn = models.TextField(max_length=50, blank=True)
    books_yn = models.TextField(max_length=50, blank=True)
    music_yn = models.TextField(max_length=50, blank=True)
    crafts_yn = models.TextField(max_length=50, blank=True)
    arts_yn = models.TextField(max_length=50, blank=True)
    learning_yn = models.TextField(max_length=50, blank=True)
    gardening_yn = models.TextField(max_length=50, blank=True)
    sports_yn = models.TextField(max_length=50, blank=True)
    exercise_yn = models.TextField(max_length=50, blank=True)
    outside_yn = models.TextField(max_length=50, blank=True)
    animals_yn = models.TextField(max_length=50, blank=True)
    socializing_yn = models.TextField(max_length=50, blank=True)
    work = models.TextField(max_length = 250, blank=True)
    volunteer = models.TextField(max_length = 250, blank=True)
    parents = models.TextField(max_length = 250, blank=True)
    siblings = models.TextField(max_length = 250, blank=True)
    close_family = models.TextField(max_length = 250, blank=True)
    spouse = models.TextField(max_length = 250, blank=True)
    children = models.TextField(max_length = 250, blank=True)
    technology = models.TextField(max_length = 250, blank=True)
    city_or_country = models.TextField(max_length = 250, blank=True)
    travel = models.TextField(max_length = 250, blank=True)
    alone_fun = models.TextField(max_length = 250, blank=True)
    social_fun = models.TextField(max_length = 250, blank=True)
    one_thing = models.TextField(max_length = 250, blank=True)