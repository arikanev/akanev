# Generated by Django 2.0 on 2018-01-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ari', '0007_auto_20171226_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(default='github.com/arikanev'),
        ),
    ]
