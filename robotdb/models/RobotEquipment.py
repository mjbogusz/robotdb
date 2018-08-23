from django.db import models
from .Equipment import Equipment
from .Robot import Robot

class RobotEquipment(models.Model):
	robot = models.ForeignKey(Robot, on_delete = models.CASCADE)
	equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE)
	available = models.BooleanField('Equipment available [Y/N]', default = False)
	notes = models.CharField('Additional notes', max_length = 2000, blank = True)

	def __str__(self):
		return str(self.robot) + ':' + str(self.equipment) + ':' + str(self.available)

	class Meta:
		unique_together = ('robot', 'equipment')
