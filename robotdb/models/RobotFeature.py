from django.db import models
from .Feature import Feature
from .Robot import Robot

class RobotFeature(models.Model):
	robot = models.ForeignKey(Robot, on_delete = models.CASCADE)
	feature = models.ForeignKey(Feature, on_delete = models.CASCADE)
	available = models.BooleanField('Feature available [Y/N]', default = False)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return str(self.robot) + ':' + str(self.feature) + ':' + str(self.available)

	class Meta:
		unique_together = ('robot', 'feature')
