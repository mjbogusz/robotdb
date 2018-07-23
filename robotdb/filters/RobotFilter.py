from django_filters import FilterSet

from robotdb.models import Robot

class RobotFilter(FilterSet):
	class Meta:
		model = Robot
		fields = {
			'name': ['contains'],
			'producer': ['contains'],
			'country': ['contains'],
			'price': ['lt', 'gt'],
		}
