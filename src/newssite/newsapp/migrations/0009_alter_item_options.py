# Generated by Django 4.2.1 on 2023-06-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': [('can_read_item', 'Can read item')]},
        ),
    ]
