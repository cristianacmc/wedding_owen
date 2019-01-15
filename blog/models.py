from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	Subject = models.CharField(max_length=200)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	#def publish(self):
    #	self.published_date = timezone.now()
    #	self.save()

	#def __str__(self):
    #    return self.email
