# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Origin(models.Model):
	name = models.CharField(max_length=50)
	year = models.PositiveIntegerField(default = 1990)
	url = models.URLField()
	
	def __unicode__(self):
		return self.name
		
class Character(models.Model):
	origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default='Affordable WAIFU at your doorstep')
	url = models.URLField()
	description = models.TextField(default='No description yet.')
	price = models.PositiveIntegerField(default=100)
	
	def __unicode__(self):
		return self.name
	
class CPhoto(models.Model):
	character = models.ForeignKey(Character, on_delete=models.CASCADE)
	description = models.TextField(default = 'Character Photo')
	url = models.URLField()
	
	def __unicode__(self):
		return self.description