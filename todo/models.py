from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Todo(models.Model):
    timeStamp=models.DateTimeField(auto_now_add=True)
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=1000)
    duedate=models.DateField(blank=True,null=True )
    Tag=TaggableManager()
    STATUS=(('OPEN','OPEN'),
        ('WORKING','WORKING'),
        ('DONE','DONE'),
        ('OVERDUE','OVERDUE'),)
    status=models.CharField(max_length=200,choices=STATUS,default="OPEN")
