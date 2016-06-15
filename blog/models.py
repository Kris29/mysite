from django.db import models
from django.utils import timezone

class Feedback(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
