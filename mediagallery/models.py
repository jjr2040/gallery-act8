# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(u'País', max_length=100)
    city = models.CharField('Ciudad', max_length=50)
    photo_url = models.URLField()


class Category(models.Model):

    name = models.CharField('Nombre', max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name 


class Media(models.Model):

    VIDEO = 1
    AUDIO = 2

    MEDIA_TYPE = (
        (VIDEO, 'Video'),
        (AUDIO, 'Audio')
    )

    url = models.URLField()
    author = models.CharField('Autor', max_length=100)
    media_type = models.IntegerField(choices=MEDIA_TYPE, verbose_name='Tipo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Fecha de creación')
    country = models.CharField(u'País', max_length=100)
    city = models.CharField('Ciudad', max_length=100)

    category = models.ForeignKey('Category', 
        related_name='category_media', 
        on_delete=models.CASCADE, 
        verbose_name=u'Categoría')
    created_by = models.ForeignKey('User', 
        related_name='user_media', 
        on_delete=models.CASCADE, 
        verbose_name='Creado por:')

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'

    def __str__(self):
        return u'%s - %s' % (self.author, self.url)

    @property
    def is_video(self):
        return self.media_type == self.VIDEO

    

class MediaClip(models.Model):

    name = models.CharField('Nombre', max_length=50)
    start_sec = models.IntegerField(default=0, verbose_name='Milisegundo de inicio')
    end_sec = models.IntegerField(verbose_name='Milisegundo de fin')

    media = models.ForeignKey('Media', related_name='clips', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Media Clip"
        verbose_name_plural = "Media Clips"

    def __str__(self):
        return self.name
    
