# Generated by Django 4.0.2 on 2022-03-24 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-author',)},
        ),
    ]
