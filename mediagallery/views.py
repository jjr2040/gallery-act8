from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class MediaListView(ListView):
    model = Media
    template_name = "mediagallery/index.html"
    context_object_name = 'media'


def details(request,id):

    mediaDetails = Media.objects.get(id = id)

    context = {
        'mediaDetails': mediaDetails
    }

    return render(request,"mediagallery/details.html", context);
