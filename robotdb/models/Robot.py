from django.db import models

class Robot(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	producer = models.CharField(max_length = 200)
	country = models.CharField('Country of origin (code)', max_length = 100, blank = True)
	link = models.CharField('Link to main site', max_length = 400, blank = True)
	videoLink = models.CharField('Link to a video', max_length = 400, blank = True)
	price = models.PositiveIntegerField('Price in EUR', default = 0, blank = True)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def save(self, *args, **kwargs):
		if self.link and self.link[0:3] != 'http':
			self.link = 'http://' + self.link
		super(models.Model, self).save(*args, **kwargs)

	def __str__(self):
		return self.name + ' (' + self.producer + ')'
