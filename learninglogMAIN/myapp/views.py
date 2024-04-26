
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import User model if not already imported



def index(request):
    return render(request, './myapp/index.html')

def inicio(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        user.save()
        if user is not None:
            login(request, user)
            return redirect('myapp:entrada')  # Redirigir al usuario a la página de inicio después del inicio de sesión
    return render(request, './myapp/inicio.html')




def registro(request):
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()

    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            print(new_user)
            return redirect('myapp:inicio')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, './myapp/registro.html', context)


# views.py

def entrada(request):
    comments = Comment.objects.all().order_by('-created_at')  
    # Ordena los comentarios por fecha de creación
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            # Guardar el comentario y asociarlo con el usuario actual
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user= request.user
                
            comment.created_at = timezone.now()
            comment.save()
            return redirect('./entrada.html')  # Redireccionar a la misma página para mostrar el comentario recién agregado
    else:
        form = CommentForm()
    return render(request, './myapp/entrada.html', {'comments': comments, 'form': form})


def eliminar_comentario(request, comments_id):
    comment = get_object_or_404(Comment, pk=comments_id)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('myapp:entrada')  # Redirect to the entrada page after deletion
    
    # If it's not a POST request, render the template with the comment object
    return render(request, 'myapp/eliminar_comentario.html', {'comment': comment})


# def editar_comentario(request,id, comments_id):
#     comment = get_object_or_404(Comment, pk=comments_id, id=id)
    
#     if request.method == 'POST':
#         # Update the comment content based on the form data
#         if comments_id:
#             form = CommentForm(instance=Comment.objects.get(id=comments_id), data=request.POST)
#         else:
#             form = CommentForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:entrada')  # Redirect to the entrada page after edit
#     else:
#         form = CommentForm(instance=comment)
    
#     # If it's not a POST request, render the template with the comment object and form
#     return render(request, 'myapp/editar_comentario.html', {'comment': comment, 'form': form})


    
def editar_comentario(request, comments_id):
    comment = get_object_or_404(Comment, pk=comments_id)  # Use 'pk' to retrieve the object
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('myapp:entrada')
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'myapp/editar_comentario.html', {'comment': comment,'form': form})

    
    
def home(request):
    return render(request, './myapp/home.html')