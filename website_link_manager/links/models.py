from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name
