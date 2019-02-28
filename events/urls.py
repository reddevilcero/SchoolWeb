from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='events'),
    path('<int:pk>/<slug:page_slug>/', EventDetailView.as_view(),
         name='event')
]
