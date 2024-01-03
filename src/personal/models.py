from django.db import models

# Create your models here.
class Question(models.Model):
	title=models.CharField(max_length=100)
	email=models.EmailField()
	question_text=models.TextField(max_length=400)
	
	

	def __str__(self):
		return self.email