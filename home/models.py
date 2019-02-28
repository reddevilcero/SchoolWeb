from django.db import models
from core.models import BaseModel


# Create your models here.
# tutor models to be used in the home view and to be linked with the clubs.
class Tutor(BaseModel):
    PROF = 'Prof.'
    DR = 'Dr.'
    MR = 'Mr.'
    MRS = 'Mrs.'
    MS = 'Ms.'
    MISS = 'Miss.'
    PROFESSION_TITLE = ((PROF, 'Prof.'),
                        (DR, 'Dr.'),
                        (MR, 'Mr.'),
                        (MRS, 'Mrs.'),
                        (MS, 'Ms.'),
                        (MISS, 'Miss.'),)
    title = models.CharField(
        verbose_name='Title', choices=PROFESSION_TITLE,
        max_length=25, blank=True, null=True)
    name = models.CharField(
        verbose_name='Name', max_length=50)
    rol = models.CharField(
        verbose_name='Occupation', max_length=50)
    description = models.CharField(
        verbose_name='Quick Description', max_length=100, default='')
    image = models.ImageField(
        verbose_name='Profile Image', upload_to='img/tutors',
        null=True, blank=True)
    facebook = models.URLField(
        verbose_name="Facebook Link", max_length=200, null=True, blank=True)
    twitter = models.URLField(
        verbose_name="Twitter Link", max_length=200, null=True, blank=True)
    instagram = models.URLField(
        verbose_name="Instagram Link", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


# Slide model for the home slider
class Slide(BaseModel):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.CharField('Description', max_length=200)
    image = models.ImageField('Image', upload_to='img/slide')

    def __str__(self):
        return self.title
