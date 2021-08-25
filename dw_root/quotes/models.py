from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from dateutil.relativedelta import relativedelta
import datetime

from django.urls import reverse


"""Модель для пользоваетля"""


class Customer(models.Model):
    IOGV_CHOICES = [
        ('KGA', 'КГА'),
        ('CIOGD', 'ЦИОГД'),
        ('NIPC', 'НИПЦ'),
    ]
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100)
    position = models.CharField('Должность', max_length=100, blank=True)
    department = models.CharField(
        'Подразделение', max_length=200, blank=True)
    iogv = models.CharField('Структура', max_length=50,
                            choices=IOGV_CHOICES, default='KGA')
    taxpayer_number = models.CharField('ИНН', max_length=50)
    snils_number = models.CharField('СНИЛС', max_length=30)
    email = models.EmailField()
    address = models.CharField('Адрес', max_length=200, blank=True)
    work_phone = models.CharField('Телефон', max_length=30, blank=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.name, self.middle_name)

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})


class GisNumber(models.Model):

    """Модель для №ГИС (пр. МАИС ЭГУ(1783) ...)"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DigitalSign(models.Model):

    """Модель для электронной подписи"""

    SIGNTYPE_CHOICES = (
        ('IAC', 'ИАЦ'),
        ('KAZN', 'Фед.Казначейство'),
    )

    customer = models.ForeignKey(Customer,
                                 blank=True,
                                 null=True,
                                 on_delete=CASCADE,
                                 verbose_name='Владелец сертификата',
                                 related_name='customer_sign')
    sign_type = models.CharField(
        'Тип подписи', max_length=100, choices=SIGNTYPE_CHOICES)
    gis_required = models.ManyToManyField(GisNumber,
                                          help_text="Выберите одну или несколько ГИС для сертификата",
                                          verbose_name='Необходимые ГИС')
    start_date = models.DateField('Дата выдачи',)
    end_date = models.DateField('Дата окончания',)
    description = models.TextField('Заметки', blank=True)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True,
                                 null=True, on_delete=models.CASCADE)

    # поле бд загрузки файла
    #jobfile = models.FileField(upload_to='', null=True, blank=True)

    class Meta:
        ordering = ['end_date']

    def __str__(self):
        return str(self.customer)
    
    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.customer.pk})


# В модели Подписи сделать поле status(Действует, Закончилась) и по статусу
# и времени до конца срока определьять сколько дней осталось до получения новой
# как только статус "Закончилась", убирать из списка для получения новых.
