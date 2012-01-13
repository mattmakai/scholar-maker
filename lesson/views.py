from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from lesson.models import Lesson, Curriculum
from lesson.forms import CreateLessonForm, CreateCurriculumForm


def list_curriculum(req):
	"""Shows a list of all curriculum."""
	curriculumList = Curriculum.objects.all()

	return direct_to_template(req, 'lesson/list_curriculum.html', \
		{'curriculumList': curriculumList,})


def show_curriculum(req, id=0, saveMsg='N'):
	"""Shows an existing curriculum if it is in the datastore."""

	showSaveMsg = False
	if saveMsg == 'Y' or saveMsg == 'y':
		showSaveMsg = True

	try:
		c = Curriculum.objects.get(id=id)
		lessons = Lesson.objects.filter(curriculum_id=c.id)
		return direct_to_template(req, 'lesson/curriculum.html', \
			{'curriculum': c, 'lessons': lessons, 'showSaveMsg': showSaveMsg })

	except ObjectDoesNotExist:
		return HttpResponse('curriculum does not exist')


def new_curriculum(req):
	"""Shows a page where a user can create a new curriculum."""
	return direct_to_template(req, 'lesson/curriculum.html')


def save_new_curriculum(req):
	"""Attempts to save a new curriculum to the datastore."""
	if req.method == 'POST':
		form = CreateCurriculumForm(req.POST)
		if form.is_valid():
			c = form.save(commit=True)
			return HttpResponseRedirect('/curriculum/show/' + str(c.id) + '/Y/')
		else:
			return HttpResponse('form is invalid')


def save_existing_curriculum(req):
	"""Attempts to update an existing curriculum."""
	if req.method == 'POST':
		id = req.POST.get('id', 0)
		name = req.POST.get('name', '')
		passPhrase = req.POST.get('pass_phrase', '')

		try:
			c = Curriculum.objects.get(id=id)
			c.name = name
			c.pass_phrase = passPhrase
			c.save()

			return HttpResponseRedirect('/curriculum/list/')

		except ObjectDoesNotExist:
			return HttpResponse('unable to find existing curriculum')
	

def new_lesson(req, curriculum_id=0):
	"""Shows a page with a blank lesson that can be filled in."""
	return direct_to_template(req, 'lesson/lesson.html', \
		{'curriculum_id': curriculum_id,})


def show_lesson(req, id=0):
	"""Attempts to retrieve an existing lesson and display it."""
	if req.method == 'POST':
		id = req.POST.get('id', 0)

	try:
		l = Lesson.objects.get(id=id)

		return direct_to_template(req, 'lesson/lesson.html', \
			{'lesson': l, 'curriculum_id': l.curriculum_id})
	except ObjectDoesNotExist:
		return HttpResponse('error retrieving lesson id')


def save_new_lesson(req, curriculum_id=0):
	"""Saves a lesson to the data store."""
	l = None

	if req.method == 'POST':
		cId = req.POST.get('curriculum_id', 0)
		form = CreateLessonForm(req.POST)
		if form.is_valid():
			try:
				c = Curriculum.objects.get(id=cId)
			except ObjectDoesNotExist:
				return HttpResponse('curriculum does not exist')

			l = form.save(commit=False)
			l.curriculum_id = c.id
			l.save()

			return HttpResponseRedirect('/curriculum/show/' + str(c.id) + '/')

		else:
			return HttpResponse('Failed. Unable to save (form invalid).')


def save_existing_lesson(req, id=0, c_id=0):
	"""Saves an existing record back to the database with updates."""
	if req.method == 'POST':
		id = req.POST.get('id', 0)
		subject = req.POST.get('subject', '')
		lesson = req.POST.get('lesson', '')
		discussion_questions = req.POST.get('discussion_questions', '')
		c_id = req.POST.get('curriculum_id', '')

		try:
			l = Lesson.objects.get(id=id)
			l.lesson = lesson
			l.subject = subject
			l.discussion_questions = discussion_questions
			l.save()

			return HttpResponseRedirect('/curriculum/show/' + str(c_id) + '/')
		except ObjectDoesNotExist:
			l = None
			return HttpResponse('not found: ' + str(id))


