# Generated by Django 3.2.3 on 2021-06-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
