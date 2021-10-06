from django.db import models
from django.utils.translation import activate

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs/',max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"File id: {self.file_name}"