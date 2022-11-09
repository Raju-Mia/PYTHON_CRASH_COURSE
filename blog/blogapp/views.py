from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
from .models import BlogPost

def blog(request):

    blogposts = BlogPost.objects.filter()
    context = {"blogpost": blogposts}
    return render(request, 'blog.html', context)


#forms import (for add the new blog)
from .forms import BlogPostform
def blogpost(request):
    if request.method != "POST":
        form = BlogPostform()

    else:
        form = BlogPostform(data=request.POST)
        if form.is_valid():
            form.save()
            print(form.save())
            return redirect('/blog/home/') #app url path name

    context = {'form': form}
    return render(request, 'blogpost.html', context)



def editblog(request, blog_id):

    blog = BlogPost.objects.get(id=blog_id)
    title_name = blog.title

    if request.method != "POST":
        form = BlogPostform(instance=blog)

    else:
        form = BlogPostform(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/home/')

    context = {"blog":blog, "title":title_name, "form":form}

    return render(request, 'editblog.html', context) 