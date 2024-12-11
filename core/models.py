from django.db import models
import shortuuid

from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.utils.text import slugify


VISIBILITY = (
    ('Only me','only me'),
    ('Everyone','everyone'),
)



def user_directory_path(instance,filename):
    ext=filename.split('.')[-1]
    filename='%s.%s' % (instance.user.id,ext)
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=500,null=True,blank=True)
    images=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    video=models.FileField(upload_to=user_directory_path,null=True,blank=True)
    visibility=models.CharField(max_length=20,choices=VISIBILITY,default='Everyone')
    active=models.BooleanField(default=True)
    
    slug=models.SlugField(unique=True,null=True,blank=True)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    views=models.PositiveIntegerField(default=0)
    pid=ShortUUIDField(length=7,max_length=25,alphabet='abcdefghjklmnopwrstuvwxyz123')
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid=uuid_key[:4]
        if self.slug == '' or self.slug == None:
            self.slug = slugify(self.title) + '-' + str(uniqueid.lower())
        super(Post,self).save(*args,**kwargs)
            
            
            
    
# class Gallery(models.Model):
#     post=models.ForeignKey(Post,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    
#     def __str__(self):
#         return str(self.post)
   
    
        
    