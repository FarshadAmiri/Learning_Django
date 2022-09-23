from django.db import models
from accounts.models import *


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return (self.filter(charity__user=user) | self.filter(assigned_benefactor__user=user) | self.filter(state='P'))



class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=((0,0),(1,1),(2,2)), default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, blank=True, null=True, choices=(('M', 'Male'), ('F', 'Female')))
    state = models.CharField(max_length=1, choices=(('P', 'Pending'),('W', 'Waiting'),('A', 'Assigned'),('D', 'Done')), default='P')
    title = models.CharField(max_length=60)

    objects = TaskManager()
