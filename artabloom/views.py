from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from .forms import edit_blog,imageform

# Create your views here.
def index(request):
    if request.method == 'POST':
        imform=imageform(request.POST,request.FILES)
        if imform.is_valid():
            imform.save()
    imform=imageform()   
    img=Blog.objects.all()
    return render(request,'home.html',{'img':img, 'imageform':imform})

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already taken!')
            return redirect('register')

        elif User.objects.filter(username=username).exists():
            messages.warning(request,'Username already taken!')
            return redirect('register')

        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
            user.save()
            messages.success(request,'Welcome to Art Abloom! You have been registered successfully.')
            return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method=="POST":
        usernamel = request.POST.get('usernamel')
        passwordl = request.POST.get('passwordl')
        user = authenticate(request, username=usernamel, password=passwordl)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid credentials or user not registered.')
            return redirect('login')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

"""
def post_blog(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        #image = request.POST.get('image')
        blog=Blog(title=title,dsc=description,user_id=request.user)
        blog.save()
        messages.success(request,'Blog posted successfully')
    return render(request,'post_blog.html')
"""

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context={'blog':blog}
    return render(request,'blog_detail.html',context)

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'Blog has been deleted')
    return redirect('/')

def edit(request,id):
    blog = Blog.objects.get(id=id)
    editblog=edit_blog(instance=blog)
    if request.method=='POST':
        form=edit_blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog edited successfully')
            return redirect('/')
    return render(request,'edit_blog.html',{'edit_blog':editblog})

def post_blog(request):
    if request.method == 'POST':
        imform=imageform(request.POST,request.FILES)
        if imform.is_valid():
            imform.save()
            return redirect('/')
    imform=imageform()   
    img=Blog.objects.all()
    return render(request,'post_blog.html',{'img':img, 'imageform':imform})
