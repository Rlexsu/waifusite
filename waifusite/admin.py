# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from waifusite import models

# Register your models here.
admin.site.register(models.Origin)
admin.site.register(models.CPhoto)

class CharacterAdmin(admin.ModelAdmin):
	list_display=('origin', 'name', 'price')
	search_fields=('name',)
	ordering=('-price',)
	
admin.site.register(models.Character, CharacterAdmin)