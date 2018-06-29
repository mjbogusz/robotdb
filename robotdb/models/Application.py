from django.db import models
from django.urls import reverse

class Application(models.Model):
	ENHANCEMENT_VALUE_CHOICES = (
		(0, 'Not present'),
		(1, 'Physical'),
		(2, 'Non-physical'),
	)

	name = models.CharField(max_length = 100, unique = True)
	mobility = models.PositiveSmallIntegerField('Mobility enhancement', default = 0, choices = ENHANCEMENT_VALUE_CHOICES)
	selfreliantCare = models.PositiveSmallIntegerField('Selfreliant care', default = 0, choices = ENHANCEMENT_VALUE_CHOICES)
	interpersonalInteraction = models.PositiveSmallIntegerField('Interpersonal interaction', default = 0, choices = ENHANCEMENT_VALUE_CHOICES)
	other = models.PositiveSmallIntegerField('Other', default = 0, choices = ENHANCEMENT_VALUE_CHOICES)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def get_absolute_url(self):
		return reverse('applicationDetail', kwargs = {'applicationID': self.pk})

	def __str__(self):
		return self.name
