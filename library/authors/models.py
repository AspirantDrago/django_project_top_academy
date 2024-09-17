from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('name', max_length=30, null=False)
    sname = models.CharField('sname', max_length=30, null=False)

    def __str__(self) -> str:
        return f'{self.name} {self.sname}'
    
    @property
    def short_name(self):
        return f'{self.sname} {self.name[:1]}.'
