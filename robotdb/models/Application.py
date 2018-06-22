from django.db import models

class Application(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	mobility = models.BooleanField('Mobility')
	selfreliantCare = models.BooleanField('Selfreliant Care')
	interpersonalInteraction = models.BooleanField('Interpersonal Interaction')
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return self.name
