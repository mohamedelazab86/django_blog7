# Generated by Django 4.2 on 2023-11-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='phot/%y-%m/%d'),
            preserve_default=False,
        ),
    ]