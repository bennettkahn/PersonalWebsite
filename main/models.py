from django.db import models

# Create your models here.
class PlaceHolder(models.Model):
	field = models.CharField(max_length=200)
