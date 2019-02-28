from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel
from ckeditor.fields import RichTextField
import datetime


# Create your models here.


class Club(BaseModel):
    name = models.CharField(_("Name"), max_length=50)
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2,
                                null=True, blank=True)
    reduced_price = models.DecimalField(_("Concesion Price"), max_digits=5,
                                        decimal_places=2, null=True,
                                        blank=True)
    start_time = models.TimeField(_("Start Time"), auto_now=False,
                                  auto_now_add=False,
                                  default=datetime.time(15, 00))
    finish_time = models.TimeField(_("Finish Time"), auto_now=False,
                                   auto_now_add=False,
                                   default=datetime.time(16, 00))
    image = models.ImageField(_("Image"), upload_to="img/clubs",
                              null=True, blank=True)
    club_tutor = models.ForeignKey("home.Tutor", verbose_name=_("Tutor"),
                                   on_delete=models.CASCADE)
    quick_description = models.CharField(_("Quick Description"),
                                         max_length=100)
    full_description = RichTextField()

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
        ordering = ['-created']

    def __str__(self):
        return self.name
