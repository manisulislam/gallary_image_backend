from django.db import models
from cloudinary.models import CloudinaryField

class ImageBox(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100,null=True)
    descriptions= models.TextField(null=True)

    def __str__(self):
        return self.title