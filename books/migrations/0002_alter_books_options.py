# Generated by Django 5.0.6 on 2024-06-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Books'},
        ),
    ]
