from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        pass

