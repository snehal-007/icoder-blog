from django.shortcuts import render ,HttpResponse ,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
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
    if len(query)>78:
       
        allPosts = Post.objects.none()

    else:
        allPosts_title = Post.objects.filter(title__icontains=query)
        allPosts_content = Post.objects.filter(content__icontains=query)

        allPosts = allPosts_title.union(allPosts_content)

    if allPosts.count() == 0:
        messages.warning(request,'No search result found Please search a correct keywords')
        
    params = {'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)  

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for error input
        if len(username) > 10:
            messages.error(request,"Your username under 10 charecters please use more charecters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"username should be letters and numbers")
            return redirect('home')    

        if pass1 != pass2:
            messages.error(request,"Your password is not match please check again")
            return redirect('home')    

        

        # Create user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been successfully created")

        return redirect('home')


    else:
        return HttpResponse('404 Not Found')    


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginUsername']
        loginpassword = request.POST['loginPassword']

        user = authenticate(username=loginusername ,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('home') 

        else:
            messages.error(request,"Invalid Credentials, Please Try again")
            return redirect('home')    



    return HttpResponse('404 Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged Out")
    return redirect('home')

    return HttpResponse('logout')    