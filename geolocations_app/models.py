from django.db import models

# Create your models here.
class AddressFile(models.Model):
    excel_file = models.FileField(upload_to='excel/')
