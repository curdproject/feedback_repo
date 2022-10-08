from django.db import models

class feedbackdata(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=100)
    feedback = models.CharField(max_length=100)
    date = models.DateField()





