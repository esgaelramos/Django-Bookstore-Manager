from django.db import models

def user_directory_path(instance, filename):
    return 'books/{0}/{1}'.format(instance.book, filename)

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    def completeName(self):
        txt = "{0} {1}"
        return txt.format(self.first_name, self.last_name)

    def __str__(self):
        return self.completeName()


class Editorial(models.Model):
    editorial = models.CharField(max_length=30)

    def __str__(self):
        return self.editorial


class Book(models.Model):
    book = models.CharField(max_length=50)

    price = models.PositiveSmallIntegerField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book', null=True)

    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='editorial_book', null=True)

    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    slug = models.SlugField(max_length=70, null=False, unique=True)

    genres = [
        ('AD', 'Adventure'),
        ('DR', 'Drama'),
        ('HU', 'Humor'),
        ('SC', 'Science'),
        ('SF', 'Science Fiction'),
        ('MY', 'Mythology'),
        ('NO', 'Novel'),
        ('PO', 'Poetry'),        
        ('RO', 'Romantic'),
        ('OT', 'Others'),
    ]
    
    genre = models.CharField(max_length=2, choices=genres, default='Others')

    published = models.DateField(default='2000-04-23', blank=True, null=True)

    code = models.CharField(primary_key=True, max_length=19) #Code in Final for a Better UX

    def __str__(self):
        text = "{0} | By {1}"
        return text.format(self.book, self.author)
    