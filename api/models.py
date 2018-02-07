from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(null=True, default=1)
    viewcount = models.IntegerField(null=True, default=1)
    tags = models.CharField(null=True, max_length=100)
    creationdate = models.DateTimeField(null=True, blank=True)
