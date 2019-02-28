from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _

# Create your models here.


class GalleryImage(BaseModel):

    name = models.CharField(_("Picture Name"), max_length=50)
    picture = models.ImageField(_("Image"), upload_to="img/gallery")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
