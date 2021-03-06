from django.db import models
from django.urls import reverse

class Project(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	link = models.CharField('Link to project', max_length = 400, blank = True)
	yearStart = models.PositiveSmallIntegerField('Start year', default = 0)
	yearEnd = models.PositiveSmallIntegerField('End year', default = 0)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def get_absolute_url(self):
		return reverse('projectDetail', kwargs = {'projectID': self.pk})

	def __str__(self):
		return self.name + ' (' + str(self.yearStart) + ' - ' + str(self.yearEnd) + ')'
