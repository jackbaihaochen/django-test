# Generated by Django 4.0.1 on 2022-01-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineauthinfo',
            name='value',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lineauthinfo',
            name='key',
            field=models.CharField(max_length=50),
        ),
    ]
