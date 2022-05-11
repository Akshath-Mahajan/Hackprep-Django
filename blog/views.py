from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.

def hello(request):
  return HttpResponse("Hello World!")

def blogList(request):
  blogs = BlogPost.objects.all()
  context = {"all_blogs": blogs}
  return render(request, 'blog_list.html', context)

def blogDetail(request, id):
  blog = BlogPost.objects.get(id=id)
  # Update number of views on blog 
  blog.views += 1
  blog.save()
  
  context = {"blog": blog}
  return render(request, 'blog_detail.html', context)