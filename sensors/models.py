from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    ip = models.CharField(max_length=15,default='0.0.0.0')
    enabled = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=False, auto_now_add=False)
    humidity = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)
