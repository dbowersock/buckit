from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
# Create your models here.

class Buser(User):
	# inherits from User
	spectrum_score = models.IntegerField(default=0)
	
class Request(models.Model):
	title = models.CharField(max_length=100)
	deadline = models.DateTimeField()
	amount = models.PositiveSmallIntegerField()
	owner = models.ForeignKey(User)
	completed = models.BooleanField(default=False)
	
	def __unicode__(self):
		return unicode(self.title)
		
	def ends_today(self):
		import datetime
		if self.deadline.date() == datetime.today.date():
			return "True"
	
class Pledge(models.Model):
	owner = models.ForeignKey(User)
	request = models.ForeignKey(Request)

class RequestAdmin(admin.ModelAdmin):
	list_display = ["title", "deadline", "amount", "owner", "completed"]
	search_fields = ["owner"]

class PledgeAdmin(admin.ModelAdmin):
	list_display = ["owner", "request"]
	search_fields = ["owner"]

class NewRequestForm(forms.Form):
	title = forms.CharField(max_length=100)
	deadline = forms.DateField()
	amount = forms.IntegerField(max_value=50, min_value=1)


admin.site.register(Request, RequestAdmin,)
admin.site.register(Pledge, PledgeAdmin)
	