from django.db import models
from django.utils import timezone
from django.core.exceptions import  ValidationError
import os
# Create your models here.
def valid_username(qw):
    name = qw.lower()
    if name[0]=='a' and (name[-1] == '1' or name[-1]== '0'):
        return qw
    else:
        raise ValidationError("Enter correct unsername(starts with a/A and end with 1/0")


def upload_path(instance, filename):
    # change the filename here is required
    return os.path.join("uploads", filename)

class TUser(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20 , unique=True , validators=[valid_username])
    join_date = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    password =models.CharField(max_length=500, null=False)

    def __str__(self):
        return f"{self.uid} , {self.username} , {self.join_date}, {self.password}"



class tasks(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(TUser , on_delete=models.PROTECT , related_name="user")
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=2000, default=None, blank=True, null=True)
    task_pic = models.ImageField(upload_to=upload_path ,default=None, blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.tid} , {self.task_title} , {self.task_description}"

