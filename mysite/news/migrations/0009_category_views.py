# Generated by Django 3.2.3 on 2021-06-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20210609_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
