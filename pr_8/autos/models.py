from django.db import models

# Create your models here.
class Auto(models.Model):
    name = models.CharField('Марка', max_length=30, null=False, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
