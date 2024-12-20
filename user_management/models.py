from django.db import models

class User(models.Model):
    company_name = models.CharField(max_length=255)
    employees = models.JSONField()  # Store employee names as a list
    positions = models.JSONField()   # Store positions as a list
    location = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.company_name