# Generated by Django 3.2.8 on 2021-10-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'ordering': ('cake_name',), 'verbose_name_plural': 'cakes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='cake',
            name='composition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
