# Generated by Django 3.2.8 on 2021-10-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211006_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='composition',
            field=models.TextField(blank=True, default='Will be added soon', null=True),
        ),
    ]
