from django.shortcuts import render ,HttpResponse

# Create your views here.


def bloghome(request):
    return render(request,'blog/blogHome.html')

def blogpost(request,slug):
    return render(request,'blog/blogPost.html')
    # return HttpResponse(f"This Blog slug is {slug}")    