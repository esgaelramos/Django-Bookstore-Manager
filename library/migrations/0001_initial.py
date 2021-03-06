# Generated by Django 4.0.2 on 2022-03-24 03:35

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editorial', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book', models.CharField(max_length=50)),
                ('price', models.PositiveSmallIntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=library.models.user_directory_path)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('genre', models.CharField(choices=[('AD', 'Adventure'), ('DR', 'Drama'), ('HU', 'Humor'), ('SC', 'Science'), ('SF', 'Science Fiction'), ('MY', 'Mythology'), ('NO', 'Novel'), ('PO', 'Poetry'), ('RO', 'Romantic'), ('OT', 'Others')], default='Others', max_length=2)),
                ('published', models.DateField(blank=True, default='2000-04-23', null=True)),
                ('code', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_book', to='library.author')),
                ('editorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editorial_book', to='library.editorial')),
            ],
        ),
    ]
