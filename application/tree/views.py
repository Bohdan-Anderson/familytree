from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from tree.models import *
from familytree.settings import MEDIA_URL

import json, datetime

def home(request):
	if request.user.is_authenticated():
		people = Person.objects.all()
		return render(request,'tree/index.html',{"data":{"people":people}})
	else:
		return redirect('/login')