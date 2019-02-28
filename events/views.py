from django.shortcuts import render
from .models import Event
from django.views.generic import DetailView, ListView

# Create your views here.


class EventListView(ListView):
    model = Event
    context_object_name = 'list_events'
    paginate_by = 3


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        context["image_list"] = event.images.all()
        context['random_event'] = Event.objects.order_by('?')[:2]
        return context
