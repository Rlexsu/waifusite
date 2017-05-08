# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse  
from waifusite import models

# Create your views here.
def index(request):
	characters = models.Character.objects.all()
	template = get_template('index.html')
	html = template.render(locals())
	return HttpResponse(html)
	
def detail(request, id):
	try:
		character = models.Character.objects.get(id=id)
		images = models.CPhoto.objects.filter(character=character)
	except:
		pass
	
	template = get_template('detail.html')
	html = template.render(locals())
	return HttpResponse(html)