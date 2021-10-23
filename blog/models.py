from django.db import models

# Create your models here.

class CV(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to="pdf's/")

    def __str__(self):
        return self.title()