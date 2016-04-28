#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from models import *


class MusicianAdmin(admin.ModelAdmin):
    list_display  = ('name', 'instrument',)
    search_fields = ('name',)
    list_filter   = ('instrument',)


class AlbumAdmin(admin.ModelAdmin):
    list_display  = ('name', 'artist', 'release_date', 'num_stars',)
    search_fields = ('name', 'artist',)
    list_filter   = ('artist',)


admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)

