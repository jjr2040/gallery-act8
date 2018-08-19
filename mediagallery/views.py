from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class MediaListView(ListView):
    model = Media
    template_name = "mediagallery/index.html"
    context_object_name = 'media'