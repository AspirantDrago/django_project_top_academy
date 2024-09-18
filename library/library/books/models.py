from django.db import models

from authors.models import Author
from readers.models import Reader
from genres.models import Genre
from typographies.models import Typography

# Create your models here.
class Book(models.Model):
    name = models.CharField('name', max_length=30, null=False)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, null=True, blank=True, on_delete=models.CASCADE)
    globalenre = models.ForeignKey(Genre, null=False, on_delete=models.CASCADE)
    typography = models.ForeignKey(Typography, null=False, on_delete=models.CASCADE)
    year = models.IntegerField('year', null=False)

    def __str__(self) -> str:
        return f'{self.author.short_name} {self.name} - {self.typography}, {self.year}'
