from django.shortcuts import render ,HttpResponse ,redirect
from blog.models import Post ,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.


def bloghome(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request,'blog/blogHome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    # exclue is a not equal to in database fetching example exclede parent none is no equal to parents its not included in
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]

        else:
            replyDict[reply.parent.sno].append(reply)    

    
    print(replyDict)
    context = {'post':post ,'comments':comments ,'user' : request.user ,'replyDict':replyDict}

    return render(request,'blog/blogPost.html',context)
    # return HttpResponse(f"This Blog slug is {slug}")    

def postComment(request):

    if request.method == 'POST':
        
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment ,user=user,post=post )
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment ,user=user,post=post,parent=parent )
            messages.success(request,"Your Reply has been posted successfully")

        comment.save()
        
    return redirect(f"/blog/{post.slug}")