# Generated by Django 4.0.2 on 2022-03-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Drama', 'Drama'), ('Humor', 'Humor'), ('Science', 'Science'), ('Science Fiction', 'Science Fiction'), ('Mythology', 'Mythology'), ('Novel', 'Novel'), ('Philosophy', 'Philosophy'), ('Poetry', 'Poetry'), ('Romantic', 'Romantic'), ('Terror', 'Terror'), ('Others', 'Others')], default='Others', max_length=20),
        ),
    ]
