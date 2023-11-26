from django.shortcuts import render,redirect
from .models import Post,Comments
from .forms import PostForm,CommentForm

# Create your views here.
#================================== crud opertions by fuction based views =============
'''
   1- list
   2- details
   3- create
   4- update
   5- delete
'''
def post_list(request):
    all_post=Post.objects.all()
    context={'post_list':all_post}
    return render(request,'posts/post_list.html',context)

def post_detail(request,id):
    my_post=Post.objects.get(id=id)
    comments=Comments.objects.filter(post=my_post)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.post=my_post
            my_form.author=request.user
            
            my_form.save()


            return redirect('/posts/')

    else:
        form=CommentForm()

    context={
        'post':my_post,
        'comments':comments,
        'form':form
        }
    return render(request,'posts/post_detail.html',context)

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')

    else:
        form=PostForm()
    
    context={'form':form}
    return render(request,'posts/create.html',context)
def update_post(request,pk):
    post=Post.objects.get(id=pk)
    
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')
    else:
        form=PostForm(instance=post)
    context={'form':form}
    return render(request,'posts/edit.html',context)
def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/posts/')

