# Generated by Django 3.2.4 on 2021-07-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='jobfile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
