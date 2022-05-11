from django.db import models
# Create your models here.

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  views = models.IntegerField(default=0)  # Number of views
  content = models.TextField()