from django.db import models
from django.urls import reverse

from .Skill import Skill
from .Article import Article
from .Equipment import Equipment
from .Project import Project

class Robot(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	producer = models.CharField(max_length = 200)
	country = models.CharField('Country of origin (3 character ISO)', max_length = 3, blank = True)
	year = models.PositiveSmallIntegerField(default = 0)
	link = models.CharField('Link to main site', max_length = 400, blank = True)
	videoLink = models.CharField('Links to videos (newline-separated)', max_length = 400, blank = True)
	price = models.PositiveIntegerField('Price in EUR', default = 0, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)
	skills = models.ManyToManyField(Skill, blank = True)
	articles = models.ManyToManyField(Article, blank = True)
	equipment = models.ManyToManyField(Equipment, blank = True)
	projects = models.ManyToManyField(Project, blank = True)

	def save(self, *args, **kwargs):
		# Add http:// prefix to links
		if self.link and self.link[0:4] != 'http':
			self.link = 'http://' + self.link
		if self.videoLink:
			links = self.videoLink.split('\n')
			for i in range(len(links)):
				if links[i][0:4] != 'http':
					links[i] = 'http://' + links[i]
			self.videoLink = '\n'.join(links)

		# Run inherited save()
		super(Robot, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('robotDetail', kwargs = {'robotID': self.pk})

	def __str__(self):
		return self.name + ' (' + self.producer + ')'
