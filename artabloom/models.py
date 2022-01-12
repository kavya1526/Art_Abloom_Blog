from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime

class Blog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=1500)
    dsc=models.TextField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="static/img/",blank=True, null=True ,default="static/img/cover.jpg")

    def __str__(self):
        return self.title