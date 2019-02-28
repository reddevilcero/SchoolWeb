from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import KeyInformation, Documents

# Create your views here.


class KeyInformationView(DetailView):
    model = KeyInformation
    template = 'keyinformation_details.html'


class DocumentsListView(ListView):
    model = Documents
    context_object_name = 'files_list'
    paginate_by = 12


class DocumentsDetailView(DetailView):
    model = Documents
