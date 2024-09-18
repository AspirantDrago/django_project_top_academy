from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Reader(models.Model):
    name = models.CharField('name', max_length=30, null=False)
    sname = models.CharField('sname', max_length=30, null=False)
    phone = PhoneNumberField('phone', null=False, unique=True, db_index=True)
    email = models.EmailField('email', max_length=30, null=False, unique=True, db_index=True)
    registration_date = models.DateField('registration_date', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.sname} ({self.email})'
