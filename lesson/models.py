from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
	"""A single unit of learning in a subject area."""
	lesson_date = models.DateTimeField(null=True, blank=True)
	subject = models.CharField(max_length=500)
	lesson = models.TextField()
	discussion_questions = models.TextField(null=True)
	curriculum_id = models.IntegerField()

	def __unicode__(self):
		return "id: " + str(self.id) + ", subject: " + str(self.subject) + \
			", lesson: " + str(self.lesson)

	def __str__(self):
		return "id: " + str(self.id) + ", subject: " + str(self.subject) + \
			", lesson: " + str(self.lesson) + ", discussion questions: " + \
			str(self.discussion_questions)
		


class Curriculum(models.Model):
	"""A series of lessons put together."""
	name = models.CharField(max_length=500, unique=True)
	pass_phrase = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	
	def __unicode__(self):
		return "name: " + str(self.name)


