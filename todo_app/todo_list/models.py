from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item