from django.db import models
from django.urls import reverse

class Feature(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	parameters = models.CharField(max_length = 400, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def get_absolute_url(self):
		return reverse('featureDetail', kwargs = {'featureID': self.pk})

	def __str__(self):
		return self.name
