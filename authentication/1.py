from django.db import models
from django.contrib.auth.models import User 









class sem2_sub(models.Model):
    sub=models.CharField(max_length=100,default=123)
    def __str__(self):
        return f'{sem2_sub.sub}'

class Sem2_subdet(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sub=models.OneToOneField(sem2_sub,on_delete=models.CASCADE)
    grade=models.CharField(max_length=100,default=123)
    attendance=models.CharField(max_length=100,default=123)
    def __str__(self):
        return f'{self.user.username} {self.sub.sub}'