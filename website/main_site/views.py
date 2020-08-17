from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main_site/index.html'

    def get_queryset(self):
        pass