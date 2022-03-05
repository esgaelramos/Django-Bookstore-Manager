# Generated by Django 4.0.2 on 2022-03-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('AD', 'Adventure'), ('DR', 'Drama'), ('HU', 'Humor'), ('SC', 'Science'), ('SF', 'Science Fiction'), ('MY', 'Mythology'), ('NO', 'Novel'), ('PH', 'Philosophy'), ('PO', 'Poetry'), ('RO', 'Romantic'), ('OT', 'Others')], default='Others', max_length=2),
        ),
    ]