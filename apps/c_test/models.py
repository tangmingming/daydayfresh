from django.db import models

# Create your models here.

class Company(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Person(models.Model):
  company = models.ForeignKey(Company, related_name="persons")
  name = models.CharField(max_length=20)
  age = models.SmallIntegerField()

  def __str__(self):
    return self.name
