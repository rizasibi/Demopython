# Generated by Django 3.2.23 on 2024-01-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dgff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
