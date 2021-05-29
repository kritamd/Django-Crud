from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=50)
    uemail=models.EmailField(max_length=50)
    upassword=models.CharField(max_length=15)

    def __str__(self):
        return self.uname