from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	contact_name = models.CharField(max_length=200)
	contact_email = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return (self.name)
