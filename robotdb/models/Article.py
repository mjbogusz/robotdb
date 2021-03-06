from django.db import models
from django.urls import reverse

class Article(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	link = models.CharField('Link to article', max_length = 400, blank = True)
	year = models.PositiveSmallIntegerField(default = 0)
	bibtex = models.CharField(max_length = 2000, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def get_absolute_url(self):
		return reverse('articleDetail', kwargs = {'articleID': self.pk})

	def __str__(self):
		name = self.name
		if (len(name) > 33):
			name = name[:30] + '...'
		return name + ' (' + str(self.year) + ')'
