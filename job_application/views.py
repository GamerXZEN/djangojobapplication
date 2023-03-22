from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.


def index(request):
	if request.method == "POST":
		form = ApplicationForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]
			date = form.cleaned_data["date"]
			occupation = form.cleaned_data["occupation"]

			Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
			                    occupation=occupation)
			messages.success(request, "Form submitted successfully!")

			message_body = f"Was it you, {first_name.capitalize()} {last_name.capitalize()} who applied to our company, " \
			               f"PythonHow. If yes, please reply to this email with YES (in uppercase). If no, immediately " \
			               f"contact newsgsnc@gmail.com to revoke the application or change it. You will go through a " \
			               f"series of tests after your job application has been reviewed an accepted to get hired at" \
			               f" PythonHow. For any questions, contact the mentioned email. We will reach out to you as soon" \
			               f" as possible.\n" \
			               f"Current Data:\n" \
			               f"Name: {last_name.capitalize()}, {first_name.capitalize()}\n" \
			               f"Email: {email}\n" \
			               f"Scheduled Start Date: {date}\n" \
			               f"Current Occupation: {occupation}\n"
			email_message = EmailMessage("Application Confirmation Email", message_body, to=[email])
			email_message.send()

	return render(request, "index.html")


def about(request):
	return render(request, "about.html")
