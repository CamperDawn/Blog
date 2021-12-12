from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Home(request):
    ctxLocal = {}
    #----------------------------------------
    # obtener los destacados para el carusel
    #----------------------------------------
    if request.user.is_authenticated:
        #----------------------------------------
        # obtener la imagen del perfil
        #----------------------------------------
        ctxLocal['user'] = request.user
    ctxLocal['range'] = range(1,19)
    return render(request,'home.html',ctxLocal)

def Search(request):
    pass

def LoginRegister(request,path):
    pass

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