from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateField(default=timezone.now)
    def __str__(self):
        return("name:{},author:{},content:{},date:{}".format(self.title,self.author,self.content,self.date_time))
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
