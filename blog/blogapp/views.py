from django.shortcuts import render, redirect

# Create your views here.
from .models import BlogPost

def blog(request):

    blogposts = BlogPost.objects.filter()
    context = {"blogpost": blogposts}
    return render(request, 'blog.html', context)


#forms import
from .forms import EditBlogform
def editblog(request):
    if request.method != "POST":
        form = EditBlogform()

    else:
        form = EditBlogform(data=request.POST)
        if form.is_valid():
            form.save()
            print(form.save())
            return redirect('/blog/home/') #app url path name

    context = {'form': form}
    return render(request, 'editblog.html', context)



