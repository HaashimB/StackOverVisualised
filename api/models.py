from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    viewcount = models.IntegerField()
    tags = models.CharField(max_length=100)
    creationdate = models.DateTimeField()

