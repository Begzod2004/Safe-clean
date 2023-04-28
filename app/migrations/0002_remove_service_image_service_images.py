# Generated by Django 4.2 on 2023-04-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='images',
            field=models.ManyToManyField(blank=True, to='app.image'),
        ),
    ]