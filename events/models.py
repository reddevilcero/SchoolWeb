from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
# Create your models here.


class Event(BaseModel):
    title = models.CharField(_("Event Name"), max_length=100)
    time = models.DateTimeField(_("Event Time"), auto_now=False,
                                auto_now_add=False)
    place = models.CharField(_("Event Place"), max_length=100)
    cover_image = models.ImageField(_("Cover Image"), upload_to="img/events")
    postcode = models.CharField(_("Event Postcode"), max_length=10)
    link = models.URLField(_("Google Maps Link to Event"), max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name=_("Event"),
                              on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_("Event Images"), upload_to="img/events")

    class Meta:
        verbose_name = 'Event Image'
        verbose_name_plural = 'Event Images'