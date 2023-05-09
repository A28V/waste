from django.shortcuts import render
from django.http import HttpResponseRedirect;
from blog.models import *
# Create your views here.
from django.contrib import messages

def blog(request,url):
	blog = Blog.objects.filter(key=url)
	return render(request,'blogs.html',{'title':'Blogs','blog':blog,'url':url})



def comments(request):
	if request.method=="POST":
   	    name = request.POST.get("name")
   	    email = request.POST.get("email")
   	    comment = request.POST.get("comment")
   	    urlkey = request.POST.get('urlkey')
   	    comment = BlogComment(name=name,email=email,comment=comment)
   	    comment.save()
   	    messages.success(request, 'Thanks for Your Feedback! '+name)
   	    return HttpResponseRedirect("/blog/"+urlkey)