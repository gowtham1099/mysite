# Generated by Django 3.0.8 on 2020-08-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Mobile_No', models.IntegerField()),
                ('Area', models.CharField(max_length=25)),
                ('Postal', models.IntegerField()),
                ('State', models.CharField(max_length=15)),
            ],
        ),
    ]
