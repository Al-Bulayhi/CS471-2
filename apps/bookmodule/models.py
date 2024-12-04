from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.city}'

class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.SmallIntegerField(default = 1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Address2(models.Model):
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.city}'

class Student2(models.Model):
    name = models.CharField(max_length = 50)
    age = models.SmallIntegerField(default = 1)
    addresses = models.ManyToManyField(Address2)

class Images(models.Model):
     coverPage = models.ImageField(upload_to='documents/')

