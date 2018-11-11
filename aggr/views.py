from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Avg
from django.db import connection

def avg(request):
	a=book.objects.aggregate(priceavg=Avg("PRICE"))
	print (a)
	print (connection.queries)
	return HttpResponse(a)
