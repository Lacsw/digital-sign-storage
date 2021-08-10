# Generated by Django 3.2.4 on 2021-08-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20210808_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='iogv',
            field=models.CharField(choices=[('KGA', 'КГА'), ('CIOGD', 'ЦИОГД'), ('NIPC', 'НИПЦ')], default='KGA', max_length=50),
        ),
    ]