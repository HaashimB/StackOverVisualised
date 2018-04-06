from django.db import models
from django.contrib.postgres.fields import JSONField


class NewTags(models.Model):
    content = JSONField()

# class Children(forms.ModelForm):
#     name = forms.CharField
#
#     class Meta:
#         model = NewTags
#         fields = ('name', 'size', 'children')

#
# class Entry(models.Model):
#     newtags = models.EmbeddedModelField(
#         model_container=NewTags,
#         model_form_class=Children
#     )
#
#     headline = models.CharField(max_length=255)
#     objects = models.DjongoManager()
