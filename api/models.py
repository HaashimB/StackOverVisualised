from django.db import models


class Post(models.Model):
    key = models.CharField(null=True, max_length=100)
    values = models.CharField(null=True, max_length=100000)


class Tags(models.Model):
    count = models.IntegerField(null=True, default=1)
    name = models.CharField(null=True, max_length=100)
