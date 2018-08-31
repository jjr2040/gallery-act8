from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from mediagallery.forms import UserCreateForm, UserUpdateForm
from .import forms

class MediaListView(ListView):
    model = Media
    template_name = "mediagallery/index.html"
    context_object_name = 'media'

def details(request,id):

    mediaDetails = Media.objects.get(id = id)
    form = forms.CreateClip

    context = {
        'mediaDetails': mediaDetails,
        'form': form
    }

    if request.method == 'POST':
        form = forms.CreateClip(request.POST)
        if form.is_valid():
            return redirect(reverse('details', args=(id,)))

    return render(request,"mediagallery/details.html", context)


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChangeUserView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('media_index')
    template_name = 'edit_user.html'

    


