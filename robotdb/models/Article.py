from django.db import models

class Article(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	link = models.CharField('Link to article', max_length = 400, blank = True)
	year = models.PositiveSmallIntegerField(default = 2018)
	bibtex = models.CharField(max_length = 2000, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return self.name + ' (' + str(self.year) + ')'
