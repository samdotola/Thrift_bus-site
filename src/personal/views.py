from django.shortcuts import render
from .import views

from personal.models import Question



def home_screen_view(request):
	if request.method == 'POST':
		title = request.POST.get('title', '')
		email = request.POST.get('email', '')
		question_text = request.POST.get('question_text', '')

		if title and email and question_text:
			question = Question(title=title, email=email, question_text=question_text)
			question.save()
			
	return render(request, 'personal/home.html', {})


	
