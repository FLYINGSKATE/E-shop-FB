from django.db import models

class Contact_details(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

    def save_this_also(self):
        self.save()