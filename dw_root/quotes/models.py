from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


"""Модель для пользоваетля"""

class Customer(models.Model):
    IOGV_CHOICES = [
    ('KGA', 'КГА'),
    ('CIOGD', 'ЦИОГД'),
    ('NIPC', 'НИПЦ'),
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=200, blank=True) #Подразделение
    iogv = models.CharField(max_length=50, choices=IOGV_CHOICES, default='KGA')
    taxpayer_number = models.CharField(max_length=50, blank=True)
    snils_number = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=200, blank=True)
    work_phone = models.CharField(max_length=30, blank=True)


"""Модель для электронной подписи"""
class DigitalSign(models.Model):
    SIGNTYPE_CHOICES = (
        ('IAC', 'ИАЦ'),
        ('KAZN', 'Фед.Казначейство'),
    )
    GIS_CHOICES = (
        ('1783', 'МАИС ЭГУ(1783)'),
        ('2693', 'ЕССК(2693)'),
    )
    STATUS_CHOICES = (
        ('active', 'Действует'),
        ('end_out', 'Закончилась'),
    )
    sign_type = models.CharField(max_length=100, choices=SIGNTYPE_CHOICES)
    gis_required = models.CharField(max_length=30, choices=GIS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField()
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True,
        null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, blank=True, 
        null=True, on_delete=CASCADE)

    #jobfile = models.FileField(upload_to='', null=True, blank=True)
    
    def __str__(self):
        return str(self.id)


    

#В модели Подписи сделать поле status(Действует, Закончилась) и по статусу
#и времени до конца срока определьять сколько дней осталось до получения новой
#как только статус "Закончилась", убирать из списка для получения новых.