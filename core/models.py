from django.db import models

# Create your models here.

class MyPost(models.Model):
	title = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	text = models.TextField(null=True)
	created_date = models.DateField(null=True)