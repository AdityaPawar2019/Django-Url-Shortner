from django.db import models

# Create your models here.
class Shortner(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15,unique=True,blank=False)
    times_followed = models.PositiveIntegerField(default = 0)


    class Meta:
        ordering = ["-date_added"]