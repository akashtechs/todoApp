from django.db import models


# Create your models here.

class ToDos(models.Model):
    date = models.TextField()
    dev_name = models.CharField(max_length=20)
    pro_name = models.CharField(max_length=50)
    pro_description = models.TextField()

    def __str__(self):
        return self.pro_name
