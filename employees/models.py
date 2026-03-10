from django.db import models
from cloudinary.models import CloudinaryField

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_joined = models.DateField()
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name