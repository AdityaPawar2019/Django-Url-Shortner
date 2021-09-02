from django.db import models
from .utils import shortened_url
# Create your models here.
class Shortner(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15,unique=True,blank=False)
    times_followed = models.PositiveIntegerField(default = 0)


    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'


    def save(self,*args,**kwargs):
        if not self.short_url:
            self.short_url = shortened_url(self)

        super().save(*args,**kwargs)