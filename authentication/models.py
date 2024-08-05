from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, default=123)
    image = models.ImageField(upload_to='profile_pic', default='default.jpeg')
    im1 = models.CharField(max_length=100, default=123)

    def __str__(self):
        return f'{self.user.username} Profile'

class sem2_sub(models.Model):
    sub = models.CharField(max_length=100, default=123)

    def __str__(self):
        return f'{self.sub}'

class sem2_subdet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub = models.ForeignKey(sem2_sub, on_delete=models.CASCADE)
    sub_code=models.CharField(max_length=100,default=123)
    P1=models.IntegerField(default=30)
    P2=models.IntegerField(default=30)
    internals=models.IntegerField(default=10)
    grade = models.CharField(max_length=100, default=123)
    attendance = models.CharField(max_length=100, default=123)
    total_classes = models.IntegerField(default=100)
    classes_present = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} {self.sub.sub}'
class sem1_sub(models.Model):
    sub = models.CharField(max_length=100, default=123)

    def __str__(self):
        return f'{self.sub}'

class sem1_subdet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub = models.ForeignKey(sem1_sub, on_delete=models.CASCADE)
    sub_code=models.CharField(max_length=100,default=123)
    P1=models.IntegerField(default=30)
    P2=models.IntegerField(default=30)
    internals=models.IntegerField(default=10)
    grade = models.CharField(max_length=100, default=123)
    attendance = models.CharField(max_length=100, default=123)
    total_classes = models.IntegerField(default=100)
    classes_present = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} {self.sub.sub}'