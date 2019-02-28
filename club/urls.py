from django.urls import path
from .views import ClubListView, ClubDetailView

urlpatterns = [
    path('', ClubListView.as_view(), name='club'),
    path('<int:pk>/<slug:page_slug>/', ClubDetailView.as_view(),
         name='club_details'),
    ]
