# Generated by Django 3.2 on 2021-10-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='resta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productos',
            name='suma',
            field=models.IntegerField(default=0),
        ),
    ]
