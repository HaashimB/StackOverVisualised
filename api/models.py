from djongo import models


class NewTags(models.Model):
    name = models.TextField()
    children = models.TextField()
