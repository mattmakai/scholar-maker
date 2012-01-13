from django.views.generic.simple import direct_to_template
from lesson.models import Curriculum

def home(req):
	"""Shows a list of all curriculum."""
	curriculumList = Curriculum.objects.all()

	return direct_to_template(req, 'index.html', \
		{'curriculum_list1': curriculumList[:7], \
		'curriculum_list2': curriculumList[7:14], \
		'curriculum_list3': curriculumList[14:21] })

