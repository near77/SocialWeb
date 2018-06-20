from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    author = models.ForeignKey(User, default = None, on_delete = models.CASCADE,related_name='%(class)s_author')
    user_image = models.FileField(null = True, blank = True, upload_to='./ProfileImage/')
    about_user = models.TextField(default = " ")
    city = models.CharField(default = '',max_length = 50)
    birthday = models.CharField(default = '',max_length = 50)
    follower = models.ManyToManyField(User,related_name='%(class)s_follower')
    follow = models.ManyToManyField(User,related_name='%(class)s_follow')
    
    def get_absolute_url(self):
        return reverse('userprofile:personal_page',kwargs = {'pk':self.author.id})
    def __str__(self):
        return str(self.author)