# Generated by Django 3.2 on 2021-10-16 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movimientos',
            fields=[
                ('id_mov', models.IntegerField(primary_key=True, serialize=False)),
                ('egreso', models.IntegerField()),
                ('ingreso', models.IntegerField()),
                ('fecha', models.CharField(max_length=10)),
                ('motivo', models.CharField(max_length=100)),
                ('prod_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id_prod', models.IntegerField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('vencimiento', models.CharField(max_length=10)),
                ('observacion', models.CharField(max_length=100)),
            ],
        ),
    ]
