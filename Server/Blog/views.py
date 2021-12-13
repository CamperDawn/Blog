from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from . import models
import re

ctxGlobal = {}
ctxGlobal['categories'] = [
    {'value':'1','category':'fin de la pobreza'},
    {'value':'2','category':'hambre cero'},
    {'value':'3','category':'salud y bienestar'},
    {'value':'4','category':'educacion de calidad'},
    {'value':'5','category':'igualdad de genero'},
    {'value':'6','category':'agua limpia y saneamiento'},
    {'value':'7','category':'energia asequible y no contaminante'},
    {'value':'8','category':'trabajo decente y crecimiento economico'},
    {'value':'9','category':'industria, innovacion e infraestructura'},
    {'value':'10','category':'reduccion de las desigualdades'},
    {'value':'11','category':'ciudades y comunidades sostenibles'},
    {'value':'12','category':'produccion y consumo responsables'},
    {'value':'13','category':'accion por el clima'},
    {'value':'14','category':'vida submarina'},
    {'value':'15','category':'vida de ecosistemas terrestres'},
    {'value':'16','category':'paz, justicia e instituciones solidas'},
    {'value':'17','category':'alianzas para lograr objetivos'},
    {'value':'18','category':'general'},
]

def imageUser(req_user):
    user = User.objects.get(username=req_user)
    profile_user = models.Profile.objects.get(usuario=user)
    return profile_user.img

def Home(request):
    ctxLocal = {}
    #----------------------------------------
    # obtener los destacados para el carusel
    #----------------------------------------
    if request.user.is_authenticated:
        ctxLocal['image_user'] = imageUser(request.user)
    ctxLocal['range'] = range(1,19)
    return render(request,'home.html',ctxLocal)

def Search(request):
    ctxLocal = {}
    ctxLocal['categories'] = ctxGlobal['categories']
    ctxLocal['types'] = [
        {'value':'1','type':'noticias'},
        {'value':'2','type':'posts'},
        {'value':'3','type':'todos'},
    ]
    ctxLocal['orders'] = [
        {'value':'1','order':'mas actual'},
        {'value':'2','order':'mas viejo'},
        {'value':'3','order':'mas comentados'},
        {'value':'4','order':'menos comentados'},
    ]
    ctxLocal['page'] = 1
    ctxLocal['more'] = False
    calc_posts = 0
    
    if request.user.is_authenticated:
        ctxLocal['image_user'] = imageUser(request.user)
    
    if request.method == 'POST':
        prev = request.POST.get('prev',None)
        next = request.POST.get('next',None)
        if prev == None:
            next = int(next)
            calc_posts = (next-1)*10
            ctxLocal['page'] = next
        elif next == None:
            prev = int(prev)
            calc_posts = (prev-1)*10
            ctxLocal['page'] = prev
    
    try:
        key_search = request.GET['search_input']
        category = int(request.GET['category'])
        type = int(request.GET['type'])
        order = int(request.GET['order'])
    except Exception as ex:
        return redirect('/search/?search_input=&category=18&type=3&order=1')
    else:
        if category < 18:
            if type < 3:
                ctxLocal['list_post'] = models.Post.objects.filter(title__icontains=key_search,
                                                                   category=category,
                                                                   post_type=type)
            else:
                ctxLocal['list_post'] = models.Post.objects.filter(title__icontains=key_search,
                                                                   category=category)
        else:
            if type < 3:
                ctxLocal['list_post'] = models.Post.objects.filter(title__icontains=key_search,
                                                                   post_type=type)
            else:
                ctxLocal['list_post'] = models.Post.objects.filter(title__icontains=key_search)
                
        if order == 1:
            ctxLocal['list_post'] = ctxLocal['list_post'].order_by('-post_date')
        elif order == 2:
            ctxLocal['list_post'] = ctxLocal['list_post'].order_by('post_date')
        elif order == 3:
            ctxLocal['list_post'] = ctxLocal['list_post'].order_by('-comment_numbers')
        else:
            ctxLocal['list_post'] = ctxLocal['list_post'].order_by('comment_numbers')
        
        more_posts = ctxLocal['list_post'][calc_posts:calc_posts+11]
        ctxLocal['list_post'] = ctxLocal['list_post'][calc_posts:calc_posts+10]
        
        if len(more_posts)>10:
            ctxLocal['more'] = True
        
    return render(request,'search.html',ctxLocal)

def LoginRegister(request,path):
    ctxLocal = {}
    if request.method == 'POST':
        redir = request.POST.get('next','home_page')
        if request.POST['action'] == 'login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect(to=redir)
            else:
                ctxLocal['userNotFound'] = True
        else:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            try:
                if User.objects.get(username=username):
                    ctxLocal['userExists'] = True
            except:
                if len(password1) >= 8 and password1 == password2:
                    if re.match(r'\w+@\w+\.com',email):
                        password_has = make_password(password1)
                        user = User.objects.create(username=username,email=email,password=password_has)
                        models.Profile.objects.create(usuario=user,img='/media/resource/user-icon.svg')
                        login(request,user)
                        return redirect(to=redir)
                    else:
                        ctxLocal['incorrectEmail'] = True
                else:
                    ctxLocal['incorrectPassword'] = True
    elif request.method == 'GET':
        logout(request)
    return render(request,'loginregister.html',ctxLocal)

def Detais(request,id_post):
    pass

@login_required(login_url='/auth/login/',redirect_field_name='next')
def Profile(request,user_name):
    pass

@login_required(login_url='/auth/login/',redirect_field_name='next')
def CreatePost(request,user_name):
    pass

@login_required(login_url='/auth/login/',redirect_field_name='next')
def Config(request,user_name):
    pass