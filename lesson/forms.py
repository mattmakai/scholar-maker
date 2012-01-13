from django import forms
from lesson.models import Curriculum, Lesson

class CreateCurriculumForm(forms.ModelForm):
	class Meta:
		model = Curriculum
		excludes = ['lesson_date',]


class CreateLessonForm(forms.ModelForm):
	class Meta:
		model = Lesson

