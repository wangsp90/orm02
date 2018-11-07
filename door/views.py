from django.shortcuts import render
from django.http import HttpResponse
from .models import *


#创建固定的等级表
def input_level(request):
	level1=level(LEVEL=1,SALARY=3000)
	level2=level(LEVEL=2,SALARY=4500)
	level3=level(LEVEL=3,SALARY=6500)
	level4=level(LEVEL=4,SALARY=8000)
	level5=level(LEVEL=5,SALARY=10000)
	level1.save()
	level2.save()
	level3.save()
	level4.save()
	level5.save()
	return HttpResponse("success!")
#创建员工表以及员工联系信息表，并分配等级
def input_employee(request):
	level1=level.objects.get(LEVEL=1)
	level2=level.objects.get(LEVEL=2)
	level3=level.objects.get(LEVEL=3)
	level4=level.objects.get(LEVEL=4)
	level5=level.objects.get(LEVEL=5)
	names=("王珏","李卫","周少华","Jill")
	for name in names:
		T=employee(NAME=name,SEX='M')
		T.LEVEL=level2
		con=contact(ADDR="GZ",NUM="18638666737")
		con.save()
		T.CONTACT=con
		T.save()
	return HttpResponse("success!")

def print(request):
	l=level.objects.get(LEVEL=2)
	es=l.employee_set.all()				#[子表值].父表名小写_set.all()可以获取所有的关联的信息
	print(type(es))
	return HttpResponse("success!")
