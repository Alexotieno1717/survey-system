from django.db import models
from django.utils import timezone
import datetime


class Survey(models.Model):
    name = models.CharField(max_length=200)
    published_on = models.DateTimeField('Published DateTime')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_on <= now

    was_published_recently.admin_order_field = 'published_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Participant(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    participation_datetime = models.DateTimeField('Participation DateTime')

    def __str__(self):
        return "Participant "+str(self.participation_datetime)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    created_on = models.DateTimeField('Creation DateTime')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    created_on = models.DateTimeField('Creation DateTime')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
