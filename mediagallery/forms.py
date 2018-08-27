from django import forms
from mediagallery.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreateForm(UserCreationForm):
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    photo_url = forms.URLField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "country", "city", "photo_url",)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user.save()
        return user


class UserUpdateForm(UserChangeForm):
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    photo_url = forms.URLField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "country", "city", "photo_url",)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserUpdateForm, self).save(commit=True)
        user.save()
        return user