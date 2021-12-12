from django.shortcuts import render

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
