from django.shortcuts import render
import random

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password_generate_list=list('abcdabcdefghijklmnñopqrstuvwxyz')
    
    acumulador_password=''
    longitud=int(request.GET.get('longitud'))
    if request.GET.get('uppercase'):
        #aqui creo una nueva lista con los valores de password_generate_list a mayuscula
        #si quiero hacerlo esto debe de estar en [] porque retorna lista
        caracter_upper=[i.upper() for i in password_generate_list]
        #la funcion extend agrega al final los valores nuevos
        password_generate_list.extend(caracter_upper)
        
    if request.GET.get('number'):
        numeros='0123456789'
        password_generate_list.extend(numeros)
        
    if request.GET.get('special'):
        char_especiales='#%$+*><='
        password_generate_list.extend(char_especiales)
        
    
    for x in range(longitud):
        acumulador_password += random.choice(password_generate_list)
        
        
        
        
    return render(request, 'generator/password.html', {'password': acumulador_password})