from django.db import models
import os

def getRobotImagePath(instance, filename):
	print(instance.robot)
	return os.path.join('robotPhotos', str(instance.robot.id), filename)

class Robot(models.Model):
	name = models.CharField(max_length = 200)
	producer = models.CharField(max_length = 200)
	country = models.CharField(max_length = 100)
	link = models.CharField(max_length = 400)
	videoLink = models.CharField('Link to a video', max_length = 400)
	notes = models.CharField(max_length = 2000)
	price = models.PositiveIntegerField(default = 0)

class RobotImage(models.Model):
	robot = models.ForeignKey(Robot, on_delete = models.CASCADE)
	image = models.ImageField(upload_to = getRobotImagePath, height_field = 'height', width_field = 'width')
	height = models.PositiveIntegerField('Image height', default = 0)
	width = models.PositiveIntegerField('Image width', default = 0)
