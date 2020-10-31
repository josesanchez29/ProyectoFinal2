from django.shortcuts import render

from .models import Slider1, Insumos, MisionyVision,Galeria

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_au
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    sliders = Slider1.objects.all()
    return render(request,'web/index.html',{'imagenes':sliders})





def galeria(request):
    galeria = Galeria.objects.all()

    sliders = Slider1.objects.all()
    return render(request,'web/galeria.html',{'imagenes':sliders, 'imageness':galeria})
    




def ubicacion(request):
    sliders = Slider1.objects.all()
    return render(request,'web/ubicacion.html',{'imagenes':sliders})






@login_required(login_url='/login/')
@permission_required('miProyectodwy.change_insumos', login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtnombre")
        precio = request.POST.get("txtprecio")
        descripcion = request.POST.get("txtdescripcion")
        stock = request.POST.get("txtstock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg='Insumo Modicado'
        except :
            msg='No Modifico Insumo '
    lista = Insumos.objects.all()
    sliders = Slider1.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista, 'msg':msg,'imagenes':sliders})        

        





@login_required(login_url='/login/')
def buscar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        sliders = Slider1.objects.all()
        return render(request,'web/formulario_insumo_modificar.html',{'insumo':insumo,'imagenes':sliders})
    except:
        msg='No existe insumo'
    lista = Insumos.objects.all()
    sliders = Slider1.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista, 'msg':msg,'imagenes':sliders})



@login_required(login_url='/login/')
@permission_required('auth.add_user',login_url='/login/')
def formulario_registro(request):
    
    if request.POST:
        nombre = request.POST.get("txtnombre")
        apellido = request.POST.get("txtapellido")
        email = request.POST.get("txtemail")
        usuario = request.POST.get("txtnombreusuario")
        contra1 = request.POST.get("txtcontraseña1")
        contra2 = request.POST.get("txtcontraseña2")
        try:
            usu = User.objects.get(username=usuario)
            sliders = Slider1.objects.all()
            return render(request,'web/formulario_registro.html',{'msg':'Usuario ya existe','imagenes':sliders})
         
        except:
            try:
                usu = User.objects.get(email=email)
                sliders = Slider1.objects.all()
                return render(request,'web/formulario_registro.html',{'msg':'Email ya existe','imagenes':sliders})
            except :
                
                if contra1!=contra2:
                 sliders = Slider1.objects.all()
                 return render(request,'web/formulario_registro.html',{'msg':'Claves no Coinciden','imagenes':sliders})
                
                usu=User()
                usu.first_name = nombre
                usu.last_name = apellido
                usu.email = email
                usu.username = usuario
                usu.set_password(contra1)

                usu.save()
                usu = authenticate(request, username=usuario, password=contra1)
                login_au(request,usu)
                sliders = Slider1.objects.all()
                return render(request,'web/index.html',{'imagenes':sliders})

    sliders = Slider1.objects.all()
    return render(request,'web/formulario_registro.html',{'imagenes':sliders})








def mision_vision(request):
    lista = MisionyVision.objects.all()
    sliders = Slider1.objects.all()
    return render(request,'web/mision_vision.html',{'imagenes':sliders,'lista':lista})
        






@login_required(login_url='/login/')
@permission_required('miProyectodwy.view_insumos', login_url='/login/')
@permission_required('miProyectodwy.delete_insumos', login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Insumo Eliminado'
    except :
        msg='No Elimino Insumo'
    lista = Insumos.objects.all()
    sliders = Slider1.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista, 'msg':msg,'imagenes':sliders})








@login_required(login_url='/login/')
@permission_required('miProyectodwy.view_insumos', login_url='/login/')
def lista_insumos(request):
    lista = Insumos.objects.all()  
    sliders = Slider1.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'imagenes':sliders})









@login_required(login_url='/login/')
@permission_required('miProyectodwy.add_insumos', login_url='/login/')
@permission_required('miProyectodwy.change_insumos', login_url='/login/')
def formulario_insumos(request):
    if request.POST:
        nombre = request.POST.get("txtnombre")
        precio = request.POST.get("txtprecio")
        descripcion = request.POST.get("txtdescripcion")
        stock = request.POST.get("txtstock")

        insumo= Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )

        insumo.save()
        sliders = Slider1.objects.all()
        return render(request,'web/formulario_insumos.html',{'msg':'Grabo Insumo correctamente','imagenes':sliders})

    sliders = Slider1.objects.all()
    return render(request,'web/formulario_insumos.html',{'imagenes':sliders})










def login(request):
    
    if request.POST:
        usuario = request.POST.get("txtnombreusuario")
        password = request.POST.get("txtcontraseña1")
        usu = authenticate(request, username=usuario, password=password)
        if usu is not None and usu.is_active:
            login_au(request,usu)

            sliders = Slider1.objects.all()
            return render(request,'web/index.html',{'imagenes':sliders})

            
        else:
            sliders = Slider1.objects.all()
            return render(request,'web/login.html',{'msg': 'No existe usuario','imagenes':sliders}) 

    sliders = Slider1.objects.all()   
    return render(request,'web/login.html',{'imagenes':sliders})











def cerrar(request):
    logout(request)
    sliders = Slider1.objects.all()
    return render(request,'web/index.html',{'imagenes':sliders})
