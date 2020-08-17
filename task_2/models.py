from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=20, blank=True)
    l_name = models.CharField(max_length=20, blank=True)
    ph_no = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)


def __str__(self):
        return self.l_name


'''class Income(models.Model):
    salary = models.IntegerField(blank=True)

    def __str__(self):
        return self.salary
'''