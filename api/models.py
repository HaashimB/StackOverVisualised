from django.db import models


class Post(models.Model):
    score = models.IntegerField(null=True, default=1)
    tags = models.CharField(null=True, max_length=100)


class Tags(models.Model):
    count = models.IntegerField(null=True, default=1)
    name = models.CharField(null=True, max_length=100)
