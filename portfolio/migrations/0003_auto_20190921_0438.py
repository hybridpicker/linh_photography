# Generated by Django 2.2.5 on 2019-09-21 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190920_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['category', 'ordering'], 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='photocategory',
            options={'ordering': ['title'], 'verbose_name': 'Photo Category', 'verbose_name_plural': 'Photo Categories'},
        ),
    ]