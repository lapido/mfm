from django.db import models

# Create your models here.
class Program(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	venue = models.CharField(max_length=200)
	time = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Testimony(models.Model):
	levels = (
			('100L', '100L'),
			('200L', '200L'),
			('300L', '300L'),
			('400L', '400L'),
			('500L', '500L'),
			('600L', '600L'),
		)
	name = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	level = models.CharField(max_length=4, choices=levels)
	testimony = models.TextField()

	def __str__(self):
		return self.name

class Gallery(models.Model):
	img_description = models.CharField(max_length=100, verbose_name="Image Description")
	image  = models.FileField(null=False)


	def __str__(self):
		return self.img_description

class Announcement(models.Model):
	announcer = models.CharField(max_length=30)
	content = models.TextField()

	def __str__(self):
		return self.announcer

class Address(models.Model):
	name = models.CharField(max_length=40)
	image = models.FileField(null=False)
	content = models.TextField()
	position = models.CharField(max_length=30)
