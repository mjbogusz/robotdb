from django.db import models

from .Application import Application
from .Article import Article
from .Feature import Feature
from .Project import Project

class Robot(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	producer = models.CharField(max_length = 200)
	country = models.CharField('Country of origin (code)', max_length = 100, blank = True)
	link = models.CharField('Link to main site', max_length = 400, blank = True)
	videoLink = models.CharField('Link to a video', max_length = 400, blank = True)
	price = models.PositiveIntegerField('Price in EUR', default = 0, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)
	applications = models.ManyToManyField(Application, blank = True)
	articles = models.ManyToManyField(Article, blank = True)
	features = models.ManyToManyField(Feature, through = 'RobotFeature', blank = True)
	projects = models.ManyToManyField(Project, blank = True)

	def save(self, *args, **kwargs):
		# Add http:// prefix to links
		if self.link and self.link[0:4] != 'http':
			self.link = 'http://' + self.link
		if self.videoLink and self.videoLink[0:4] != 'http':
			self.videoLink = 'http://' + self.videoLink

		# Run inherited save()
		super(Robot, self).save(*args, **kwargs)

	def __str__(self):
		return self.name + ' (' + self.producer + ')'
