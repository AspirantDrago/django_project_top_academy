from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=255)
    text = models.TextField('Текст')
    datetime = models.DateTimeField('Дата публикации')
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/posts/{self.id}'
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        