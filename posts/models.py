from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import datetime



# Create your models here.
class Post(models.Model):
    
    title=models.CharField(max_length=100,verbose_name=_('name_post'))
    content=models.TextField(max_length=1000)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(auto_now=True)

    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    image=models.ImageField(upload_to='phot/%y-%m/%d')
    tags = TaggableManager()
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='post_category')


    
    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments_post')
    content=models.TextField(max_length=500)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments_author')
    publish_date=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.post)
