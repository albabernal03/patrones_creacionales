from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.utils.translation import activate


# Create your views here.

class VRegistro(View):
    def get(self,request):

        activate('es')

        form= UserCreationForm()

        return render(request,'registro/registro.html',{'form':form})

    def post(self,request):
        activate('es')
        
        form= UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request,usuario)

            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request, 'registro/registro.html', {'form':form})
            

