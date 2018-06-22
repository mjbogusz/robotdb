from django.db import models

class Feature(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	parameters = models.CharField(max_length = 400)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return self.name
