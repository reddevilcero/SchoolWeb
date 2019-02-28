from django.shortcuts import render
from django.views.generic import ListView
from .models import GalleryImage

# Create your views here.


class GalleryImageListView(ListView):
    model = GalleryImage
    template_name = "gallery/gallery.html"
    context_object_name = 'gallery'
    paginate_by = 2
