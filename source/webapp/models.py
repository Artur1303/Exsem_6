from django.db import models
from django.core.validators import MinValueValidator

STATUS_CHOICES = [
    ('active', 'Активное'),
    ('blocked', 'Заблокировано')]


class Bock(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    text = models.CharField(max_length=500, verbose_name='Запись')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время  создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновление')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
