from django.db import models

# Create your models here.
class Adduser(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=40)
    pic = models.ImageField()

    def __str__(self):
        return "{}".format(self.email)
