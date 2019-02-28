from django.shortcuts import render
from django.views.generic import DetailView
from .models import ParentsInformation

# Create your views here.


class ParentsInforamtionView(DetailView):
    template_name = "parents_zone/parents_informations.html"
    model = ParentsInformation
