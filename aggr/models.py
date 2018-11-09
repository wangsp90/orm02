from django.db import models
#级表是固定的，员工表是员工信息，还有员工的联系方式表

class author(models.Model):
	NAME=models.CharField(null=False,max_length=255)
	class Meta:
		db_table='author'

class publisher(models.Model):
	NAME=models.CharField(null=False,max_length=255)
	class Meta:
		db_table='publisher'
		
class book(models.Model):
	NAME=models.CharField(null=False,max_length=255)
	PRICE=models.FloatField()
	COUNTRY=models.CharField(max_length=255)
	AUTHOR=models.ForeignKey(author,on_delete=models.CASCADE)
	PUBLISHER=models.ForeignKey(publisher,on_delete=models.CASCADE)
	class Meta:
		db_table='book'		

class order(models.Model):
	NAME=models.CharField(null=False,max_length=255)
	PRICE=models.FloatField()
	class Meta:
		db_table='order'


    