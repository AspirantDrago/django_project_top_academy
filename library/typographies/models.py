from django.db import models

# Create your models here.
class Typography(models.Model):
    name = models.CharField('name', max_length=30, null=False, unique=True)

    def __str__(self) -> str:
        return self.name