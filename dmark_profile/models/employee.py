from django.db import models

class Employee(models.Model):
    applied_for = models.CharField(max_length=200)
    first_name_taken = models.CharField(max_length=200)
    last_name_taken = models.CharField(max_length=200)
    phone_number_taken = models.CharField(max_length=200)
    email_id_taken = models.EmailField(max_length=200)
    description_taken = models.CharField(max_length=300, default=None)

    def save_this(self):
        self.save()