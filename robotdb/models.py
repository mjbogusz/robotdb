from django.db import models
import os

def getRobotImagePath(instance, filename):
	print(instance.robot)
	return os.path.join('robotPhotos', str(instance.robot.id), filename)

class Robot(models.Model):
	name = models.CharField(max_length = 200)
	producer = models.CharField(max_length = 200)
	country = models.CharField(max_length = 100, blank = True)
	link = models.CharField(max_length = 400, blank = True)
	videoLink = models.CharField('Link to a video', max_length = 400, blank = True)
	notes = models.CharField(max_length = 2000, blank = True)
	price = models.PositiveIntegerField('Price in EUR', default = 0, blank = True)

class RobotImage(models.Model):
	robot = models.ForeignKey(Robot, on_delete = models.CASCADE)
	image = models.ImageField(upload_to = getRobotImagePath, height_field = 'height', width_field = 'width')
	height = models.PositiveIntegerField('Image height', blank = True)
	width = models.PositiveIntegerField('Image width', blank = True)
