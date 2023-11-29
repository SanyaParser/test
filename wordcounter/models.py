from django.db import models

class LoadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')