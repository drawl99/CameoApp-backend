# Generated by Django 2.2.10 on 2020-03-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameos', '0002_auto_20200325_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameo',
            name='url_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
