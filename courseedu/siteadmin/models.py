from django.db import models
from django.conf import settings
from django.conf.urls.static import static

class coursecategories(models.Model):
    sno=models.IntegerField(unique=True,blank=True)
    name=models.CharField(max_length=128,blank=True,null=True)
    short_name=models.CharField(max_length=32,blank=True,null=True)
    content_id=models.CharField(max_length=32,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    is_visible=models.BooleanField(default=True)
    selection=models.BooleanField(default=False)
    img=models.ImageField(blank=True, upload_to='categories')