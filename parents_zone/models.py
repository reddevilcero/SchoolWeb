from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _

# Create your models here.


class ParentsInformation(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    content = RichTextField(_("Content"))
    published = models.DateTimeField(_("Published"), default=now)
    image = models.ImageField(_("Image"), upload_to="img/parents_zone",
                              blank=True, null=True)
    author = models.ForeignKey(User, verbose_name=_("Author"),
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Parerents Information'
        verbose_name_plural = 'Parerents Informations'
        ordering = ['-created']

    def __str__(self):
        return self.title
