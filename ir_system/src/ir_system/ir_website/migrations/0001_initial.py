# Generated by Django 3.1.4 on 2020-12-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmilyDickinson',
            fields=[
                ('id', models.IntegerField(default=-1, primary_key='True', serialize=False)),
                ('document', models.TextField()),
            ],
        ),
    ]
