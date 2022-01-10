# Generated by Django 4.0.1 on 2022-01-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('expiry', models.CharField(max_length=344)),
            ],
            options={
                'verbose_name': 'Ball',
                'db_table': 'Home_ball',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField()),
                ('transactiondate', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Bank',
                'db_table': 'Home_bank',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghgkeg', models.CharField(max_length=444)),
            ],
            options={
                'verbose_name': 'Car',
                'db_table': 'Home_car',
            },
        ),
        migrations.CreateModel(
            name='Modelnames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thunder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightspeed', models.IntegerField()),
                ('lightcolor', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Thunder',
                'db_table': 'Home_thunder',
            },
        ),
        migrations.CreateModel(
            name='Vertigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sky', models.CharField(max_length=344)),
            ],
            options={
                'verbose_name': 'Vertigo',
                'db_table': 'Home_vertigo',
            },
        ),
    ]
