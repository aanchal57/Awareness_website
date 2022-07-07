from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField()
    body=models.TextField()
    descript=models.TextField()
    auth_detail=models.TextField()

    def __str__(self):
        return self.title +' | '+ str(self.author)
class Comments(models.Model):
    comm=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    Name=models.CharField(max_length=255)
    Mail_id=models.EmailField()
    Message=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '% s -%s' % (self.comm.title, self.Name)

