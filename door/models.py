from django.db import models
#级表是固定的，员工表是员工信息，还有员工的联系方式表

class article(models.Model):
	NAME=models.CharField(null=False,max_length=255)
	CONTENT=models.TextField()
	class Meta:
		db_table='article'
			



    