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

def orderby(request):
	#根据价格从小到大排序
	book04=book.objects.order_by("PRICE")
	for b in book04:
		print ("%s/%s" % (b.NAME,b.PRICE))
	#根据价格从大到小排序
	book05=book.objects.order_by("-PRICE")
	for b in book05:
		print ("%s/%s" % (b.NAME,b.PRICE))
	#根据book表中的PRICE排序
	od=order.objects.order_by("NAME__PRICE")
	for o in od:
		print ("%s/%s" % (o.NAME.NAME,o.PRICE))	
	return HttpResponse("Good!")