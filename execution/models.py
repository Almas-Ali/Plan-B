from django.db import models
from django.utils.timezone import now

# Create your models here.


class Profile(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, default='')
    age = models.IntegerField(verbose_name='Age', default=0)
    gender = models.CharField(verbose_name='Gender', max_length=20, default='')
    username = models.CharField(
        verbose_name='Username', max_length=15, unique=True, default='')
    nationality = models.CharField(
        verbose_name='Nationality', max_length=30, default='')
    height = models.CharField(verbose_name='Height', max_length=15, default=0)
    hair_color = models.CharField(
        verbose_name='Hair Color', max_length=20, default='')
    bio = models.TextField(verbose_name='Bio', max_length=5000, default='')
    occupation = models.CharField(
        verbose_name='Occupation', max_length=50, default='')
    address = models.TextField(
        verbose_name='Address', max_length=300, default='')
    image = models.ImageField(verbose_name='Image', upload_to='Image')
    social = models.TextField(
        verbose_name='Social Links', max_length=5000, default='')
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
