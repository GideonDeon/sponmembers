# Generated by Django 4.0.3 on 2022-04-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Serial',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
