from django import forms
from cars.models import Car

class ListForm(forms.ModelForm):
	class Meta:
		model = Car
		exclude = [""]

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Car
		exclude = [""]