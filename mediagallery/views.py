from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from mediagallery.forms import UserCreateForm

class MediaListView(ListView):
    model = Media
    template_name = "mediagallery/index.html"
    context_object_name = 'media'

class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'