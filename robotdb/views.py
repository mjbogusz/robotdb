from django.http import HttpResponse
from django.template import loader
from .models import Robot

def index(request):
	template = loader.get_template('robotList.html')
	context = {
		'robotList': Robot.objects.all()
	}
	return HttpResponse(template.render(context, request))

def robotDetail(request, robotID):
	return HttpResponse('Robot %s' % (robotID))
