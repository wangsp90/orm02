from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Avg
from django.db import connection
from django.db.models import Q,F

def avg(request):
	a=book.objects.aggregate(priceavg=Avg("PRICE"))
	print (a)
	print (connection.queries)
	return HttpResponse(a)

def queryset(request):
	#查找ID大于2的图书，又不等于3的图书
	'''方法一，使用Q表达式
	book01=book.objects.filter(id__gte=2)
	book02=book01.filter(~Q(id=3))
	for b in book02:
		print ("《%s》" % b.NAME)
	'''
	'''方法二，链式调用	
	book01=book.objects.filter(id__gte=2).filter(~Q(id=3))
	for b in book01:
		print ("《%s》" % b.NAME)
	'''
	#方法三，exclude
	book02=book.objects.filter(id__gte=2).exclude(id=3)
	for b in book02:
		print ("《%s》" % b.NAME)
	book03=book.objects.annotate(author=F("AUTHOR__NAME"))
	for b in book03:
		print ("《%s》%s" % (b.NAME,b.author))

	return HttpResponse("success!")
