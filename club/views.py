from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Club
# Create your views here.


class ClubListView(ListView):
    model = Club
    template_name = 'club/club_list.html'


class ClubDetailView(DetailView):
    model = Club
    template_name = 'club/club_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        context['random_club'] = Club.objects.order_by('?')[:2]
        return context
