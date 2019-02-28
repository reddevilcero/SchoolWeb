from django.shortcuts import render
from .models import Tutor, Slide
from club.models import Club

# Create your views here.


def home(request):
    tutors = Tutor.objects.order_by('?').all()
    slides = Slide.objects.order_by('?').all()
    clubs = Club.objects.all()
    return render(request, 'home/home.html',
                  {'tutors': tutors,
                  'slides': slides,
                  'clubs': clubs})
