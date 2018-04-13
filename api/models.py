from django.db import models
from django.contrib.postgres.fields import JSONField


class FebJson(models.Model):
    id = models.AutoField(primary_key=True)
    content = JSONField()


class MarJson(models.Model):
    id = models.AutoField(primary_key=True)
    content = JSONField()


class JanJson(models.Model):
    id = models.AutoField(primary_key=True)
    content = JSONField()


class JanCsv(models.Model):
    id = models.AutoField(primary_key=True)
    tags = models.CharField(max_length=10000)
    score = models.IntegerField()
