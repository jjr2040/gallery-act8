from django import forms
from mediagallery.models import User, MediaClip
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    country = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    photo_url = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "country", "city", "photo_url")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user.save()
        return user


class UserUpdateForm(ModelForm):
    photo_url = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "country", "city", "photo_url")

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserUpdateForm, self).save(commit=True)
        user.save()
        return user


class CreateClip(ModelForm):

    class Meta:
        model = MediaClip
        fields = ("name", "start_sec", "end_sec")
