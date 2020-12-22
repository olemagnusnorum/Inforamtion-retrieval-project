from django.db import models

# Create your models here.

#i dont believe i need models/database as all my info is in the files and saved matrix models

class EmilyDickinson(models.Model):
    id = models.IntegerField(default=-1, primary_key="True")
    document = models.TextField()


class TalesFromTheNorse(models.Model):
    id = models.IntegerField(default=-1, primary_key="True")
    document = models.TextField()

class ItalianRecipes(models.Model):
    id = models.IntegerField(default=-1, primary_key="True")
    document = models.TextField()