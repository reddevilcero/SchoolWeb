from django.db import models
from core.models import BaseModel
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(BaseModel, HitCountMixin):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    published = models.DateTimeField(verbose_name='Published', default=now)
    hit_count = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_relation')
    image = models.ImageField(
        verbose_name='Image', upload_to='img/blog',
        null=True, blank=True)
    author = models.ForeignKey(
        User, verbose_name='Autor',
        on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, verbose_name='Categories',
        related_name='get_posts', blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def __str__(self):
        return self.title
