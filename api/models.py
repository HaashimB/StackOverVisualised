from django.db import models
from django.contrib.postgres.fields import JSONField


class NewTags(models.Model):
    content = JSONField()
