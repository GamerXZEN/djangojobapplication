from django import forms


class ApplicationForm(forms.Form):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	email = forms.EmailField()
	date = forms.DateField()
	occupation = forms.CharField(max_length=255)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
