from django.contrib.auth import get_user_model
from django.db import models
from autoslug import AutoSlugField
# from ckeditor.fields import RichTextField


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    slug = AutoSlugField(populate_from='title')
    thumbnail = models.ImageField(upload_to="", null=True, blank=True)
    image_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    overview = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()

    def __str__(self):
        return self.title
