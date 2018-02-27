from django.db import models


class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(null=True, default=1)
    viewcount = models.IntegerField(null=True, default=1)
    tags = models.CharField(null=True, max_length=100)
    creationdate = models.DateTimeField(null=True, blank=True)


class Tags(models.Model):
    count = models.IntegerField(null=True, default=1)
    name = models.CharField(null=True, max_length=100)
