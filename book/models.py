from django.db import models

# Create your models here.

class Book (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100, default='')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Author (models.Model):
    GENDER_CHOICES = (
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other"),
            ("A", "Attack Helicopter"),
        )

    gender = models.CharField(max_length = 1,choices = GENDER_CHOICES, default='Attack Helicopter')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

class Category (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(max_length=255, blank=True, default='')
    author = models.TextField(max_length=255, blank=True, default='')

class Meta:
    ordering = ['created']