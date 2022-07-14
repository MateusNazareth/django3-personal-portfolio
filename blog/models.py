from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField(default=None)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
