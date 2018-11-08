from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def exact(request):
	#使用filter方法查询
	#返回一个<QuerySet [<article: article object (1)>]>，类似list\dict
	a1=article.objects.filter(id__exact=1)
	print(a1)
	'''
	#查看使用的sql原始语句
	#SELECT * WHERE `article`.`id` = 1
	print(a1.query)
	'''
	'''
	#使用get方法查询
	#返回一个article object (1)，只返回一个
	a2=article.objects.get(id__exact=1)
	print(a2)
	'''
	'''
	#iexact，sql原始语句为：
	#SELECT * LIKE xxxx
	a3=article.objects.filter(CONTENT__iexact="XXXXXXXXXXXXXX")
	print (a3)
	'''
	a4=article.objects.filter(CONTENT__icontains="xxxx")
	print (a4)
	return HttpResponse("Good!")	

