from django.conf import settings
from django.db import models
User=settings.AUTH_USER_MODEL





VISIBILITY = (
    ('Only me','only me'),
    ('Everyone','everyone'),
)





class Post(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    images=models.ImageField(upload_to='images',null=True,blank=True)
    visibility=models.CharField(max_length=20,choices=VISIBILITY,default='Everyone')
    
    
    
    def __str__(self):
        return self.title
    
    
            
            
    
# class Gallery(models.Model):
#     post=models.ForeignKey(Post,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    
#     def __str__(self):
#         return str(self.post)
   
    
        
    