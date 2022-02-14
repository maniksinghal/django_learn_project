from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blog_objs = Blog.objects.all()
    #or Blog.objects.order_by('-date')[:5]  #Get last 5 objects, not all
    return render(request, 'mysite_blog/home.html',
                   {'blogs' : blog_objs})

def detail(request, blog_id):
    #Search internal sqlite blog-database for primary-key=blog-id
    # (so primary-key increments from 1,2,3.. i guess)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'mysite_blog/detail.html', 
                {'blog':blog})
