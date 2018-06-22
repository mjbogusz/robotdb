import os

def getRobotImagePath(instance, filename):
	return os.path.join('robotPhotos', str(instance.robot.id), filename)
