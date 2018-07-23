import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from .Robot import Robot
from .utils import getRobotImagePath

class RobotImage(models.Model):
	robot = models.ForeignKey(Robot, on_delete = models.CASCADE)
	image = models.ImageField(upload_to = getRobotImagePath, height_field = 'height', width_field = 'width', unique = True)
	thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFit(100, 100)], format = 'JPEG', options = {'quality': 90})
	description = models.CharField('Image description', max_length = 200, blank = True)
	height = models.PositiveIntegerField('Image height', blank = True)
	width = models.PositiveIntegerField('Image width', blank = True)

	def __str__(self):
		name = self.robot.name
		if (self.description):
			name += ':' + self.description
		else:
			name += ':' + os.path.basename(self.image.file.name)
		return name
