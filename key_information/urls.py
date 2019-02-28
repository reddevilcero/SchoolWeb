from django.urls import path
from . import views

urlpatterns = [
    # url path for key_information app
    path('<int:pk>/<slug:title_slug>/',
         views.KeyInformationView.as_view(), name="Information"),
    path('archive/', views.DocumentsListView.as_view(), name="archive"),
    path('archive/<int:pk>/<slug:page_slug>/',
         views.DocumentsDetailView.as_view(), name="file"),


]