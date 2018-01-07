# Generated by Django 2.0 on 2018-01-07 21:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ari', '0010_auto_20180106_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='Tell us about yourself.                            If you are concerned with internet anonymity,                            consider leaving this blank')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.Bio')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.Email')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.Image')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.URL')),
            ],
        ),
        migrations.CreateModel(
            name='User_ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^\\w{4,6}$')])),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='email',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ari.User_ID'),
        ),
    ]