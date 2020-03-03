from django.shortcuts import render ,HttpResponse
from blog.models import Post

# Create your views here.


def bloghome(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request,'blog/blogHome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}

    return render(request,'blog/blogPost.html',context)
    # return HttpResponse(f"This Blog slug is {slug}")    