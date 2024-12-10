from django.db import models

from shortuuid.django_fields import ShortUUIDField
from userauths.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500,null=True,blank=True)
    images=models.ImageField(upload_to=)
    video=models.FileField()
    visibility=models.CharField()
    active=models.BooleanField()
    
    slug=models.SlugField()
    likes=models.PositiveIntegerField()
    views=models.PositiveIntegerField()
    pid=ShortUUIDField()
    date=models.DateTimeField()
    
    def __str__(self):
        return self.title
    
        
    