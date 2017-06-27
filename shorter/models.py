from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class TargetURL(models.Model):

    url = models.URLField()

    def __str__(self):
        return self.url
