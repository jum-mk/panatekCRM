# Generated by Django 3.2.14 on 2022-07-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20220707_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
