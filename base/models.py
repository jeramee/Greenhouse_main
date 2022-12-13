from django.db import models
from django.utils.translation import gettext as _
'''from django.conf import settings'''

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Vegetable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Herb(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Greenhouse(models.Model):
    name = models.CharField(max_length=200)
    fruits = models.ManyToManyField(Fruit)
    herbs = models.ManyToManyField(Herb)
    vegetables = models.ManyToManyField(Vegetable)
    devices = models.ManyToManyField(Device)
    body = models.TextField()

    def __str__(self):
        return self.name

'''Not sure if this is needed I am leaning towards no 
because this will not be viewable just a way to
write the inventory to file. It will also be stored in
the database. '''
class Gh1_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh2_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh3_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh4_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh5_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh6_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

class Gh7_Dict(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dictionary = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.name

