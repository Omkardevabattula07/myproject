from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField( max_length=50)
    number=models.IntegerField()
    image=models.ImageField( upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name