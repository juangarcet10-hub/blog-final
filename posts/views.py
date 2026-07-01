from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from .forms import PostForm, PerfilForm
from .models import Post, Perfil

def lista_posts(request):
    posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
    return render(request, 'posts/lista.html', {'posts': posts})

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'posts/detalle.html', {'post': post})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito. Ya podés iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'posts/registro.html', {'form': form})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'Post creado con éxito.')
            return redirect('detalle_post', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'posts/form_post.html', {'form': form, 'titulo_pagina': 'Nuevo post'})


@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post actualizado.')
            return redirect('detalle_post', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form_post.html', {'form': form, 'titulo_pagina': 'Editar post'})
@login_required
def perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'posts/perfil.html', {'form': form})