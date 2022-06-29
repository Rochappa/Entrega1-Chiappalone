from django.shortcuts import render, HttpResponse
from ProApp.models import Autos, Motos, Camiones
from ProApp.forms import AutoFormulario, MotoFormulario, CamionesFormulario


def inicio(request):

    return render(request, 'ProApp/inicio.html')

def autos(request):

    if request.method == 'POST':

        mi_formulario = AutoFormulario(request.POST)

        
        if mi_formulario.is_valid():

            info_auto = mi_formulario.cleaned_data

            auto = Autos (marca=info_auto['marca'], modelo=info_auto['modelo'], anio=info_auto['anio'], color=info_auto['color'])

            auto.save()

            return render(request, 'ProApp/inicio.html')

    else:

        mi_formulario = AutoFormulario()

    return render(request, 'ProApp/autos.html', {'miformulario':mi_formulario}) 


    
def motos(request):

    if request.method == 'POST':

        mi_formulario = MotoFormulario(request.POST)

        
        if mi_formulario.is_valid():

            info_moto = mi_formulario.cleaned_data

            moto = Motos (marca=info_moto['marca'], modelo=info_moto['modelo'], cilindrada=info_moto['cilindrada'], anio=info_moto['anio'])

            moto.save()

            return render(request, 'ProApp/inicio.html')

    else:

        mi_formulario = MotoFormulario()

    return render(request, 'ProApp/motos.html', {'miformulario':mi_formulario})

def camiones(request):

    if request.method == 'POST':

        mi_formulario = CamionesFormulario(request.POST)

        
        if mi_formulario.is_valid():

            info_camion = mi_formulario.cleaned_data

            camion = Camiones (marca=info_camion['marca'], modelo=info_camion['modelo'], anio=info_camion['anio'], carga_total=info_camion['carga_total'])

            camion.save()

            return render(request, 'ProApp/inicio.html')

    else:

        mi_formulario = CamionesFormulario()

    return render(request, 'ProApp/camiones.html', {'miformulario':mi_formulario})


def buscar(request):
    
    if request.GET['busca']:

        modelo = request.GET['busca']

        autos = Autos.objects.filter(modelo__icontains=modelo)
        


        return render(request, "ProApp/resultado_busqueda.html", {"autos":autos, "modelo":modelo})
        
    
    else:

        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)




    

        



