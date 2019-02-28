from django.urls import path
from .views import ParentsInforamtionView

urlpatterns = [
    path('<int:pk>/<slug:page_slug>/', ParentsInforamtionView.as_view(),
         name='parents_zone'),
]
