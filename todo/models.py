from django.db import models
from django.urls import reverse


# Create your models here.

class ToDos(models.Model):
    pro_id = models.AutoField(primary_key=True)
    date = models.TextField()
    dev_name = models.CharField(max_length=20)
    pro_type = models.CharField(max_length=20)
    pro_name = models.CharField(max_length=50)
    pro_description = models.TextField()

    def __str__(self):
        return self.pro_name


class Files(models.Model):
    pro_id = models.ForeignKey(ToDos, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')

    @property
    def filename(self):
        name = self.file.name.split("/")[1].replace('_', ' ').replace('-', ' ')
        return name

    def get_absolute_url(self):
        return reverse('myapp:document-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.file.name
