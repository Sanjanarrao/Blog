from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def home(request):
	all_posts=Post.objects.all()
	return render(request,"home.html",{'all_posts':all_posts})
def how(request):
	return HttpResponse("how do you do")
def heya(request):
	return HttpResponse("How are you?")
def about(request,name):
	response=render(request,"about.html",{'person':name})
	print(type(response))
	return response
# Create your views here.
def create_post(request):
	if request.method=="POST":
		title=request.POST['title']
		return HttpResponse(title)
	return render(request,"create.html")