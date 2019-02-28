from django.db import models
from parents_zone.models import BaseModel
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class KeyInformation(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    published = models.DateTimeField(verbose_name='Published', default=now)
    image = models.ImageField(verbose_name='Image', upload_to='img/blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Key Information'
        verbose_name_plural = 'Key Informations'

    def __str__(self):
        return self.title
        

class Documents(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    published = models.DateTimeField(verbose_name='Published', default=now)
    archive = models.FileField(verbose_name='Document to Upload', upload_to='file', max_length=100)

    class Meta:
        verbose_name = 'Document to Upload'
        verbose_name_plural = 'Documents to Upload'
        ordering = ['-published']

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title