from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

class VRegistro(View):
    def get(self,request):
        form= UserCreationForm()
        #Cambiamos las etiquetas de los campos a español
        form.fields['username'].label='Nombre de usuario'
        form.fields['password1'].label='Contraseña'
        form.fields['password2'].label='Confirmar contraseña'
        
        return render(request,'registro/registro.html',{'form':form})

    def post(self,request):
        form= UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request,usuario)

            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request, 'registro/registro.html', {'form':form})
            

