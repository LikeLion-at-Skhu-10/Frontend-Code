from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    imgfile = models.ImageField(null = True,upload_to = "",blank = True)

    def __str__(self):
        return self.title

class date(models.Model):
    monday = models.BooleanField(default = False)
    thesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
