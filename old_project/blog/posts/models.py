from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    anons = models.CharField(verbose_name='Анонс', max_length=255)
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to="posts_image", verbose_name="Картинка", blank=True, null=True)
    datetime = models.DateTimeField('Дата публикации')
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/posts/{self.id}'
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        