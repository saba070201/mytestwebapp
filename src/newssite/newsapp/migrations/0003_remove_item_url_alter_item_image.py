# Generated by Django 4.2.1 on 2023-05-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_item_date_subitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='url',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='newsapp/images'),
        ),
    ]
