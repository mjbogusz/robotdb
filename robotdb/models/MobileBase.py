from django.db import models

class MobileBase(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return self.name
