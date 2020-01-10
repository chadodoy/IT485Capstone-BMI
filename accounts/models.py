from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# from django.db import models
# class Article(models.Model):
#     category = models.ForeignKey('Category', on_delete=models.PROTECT)
#     title =  models.CharField(max_length=55)
#     # ...
    
#     def __str__(self):
#         return self.title

class BmiInfo(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi_info = models.DecimalField(max_digits=5, decimal_places=2)
    bmi_stat = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)
    

# Create your models here.

# class Account(models.Model)
# 	email = models.CharField(max_length=30)
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	height = models.IntegerField()
# 	weight = models.IntegerField()
