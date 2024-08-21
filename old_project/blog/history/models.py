from django.db import models

# Create your models here.

class History(models.Model):
    title = models.CharField('title', max_length=100)
    anons = models.CharField('anons', max_length=255)
    full_story = models.TextField('full_story')
    datetime = models.DateField('datetime')
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'История'
        verbose_name_plural = "Истории"