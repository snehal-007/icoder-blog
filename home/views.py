from django.shortcuts import render ,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.


def home(request):

    return render(request,'home/home.html')
    # return HttpResponse("Thats Blog home")

def about(request):
    messages.error(request,'this is about')
    return render(request,'home/about.html')  

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        content = request.POST.get('content','')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request,'Please fill correct details')

        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your details has been Submit successfully Thank You")



        
        return render(request,'home/contact.html') 

    return render(request,'home/contact.html')        


def search(request):
    # post = Post.objects.all()
    query = request.GET['query']
    post = Post.objects.filter(title__icontains=query)
    params = {'allPost':post}

    return render(request,'home/search.html',params)  