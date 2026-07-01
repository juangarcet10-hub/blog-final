from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
    return render(request, 'posts/lista.html', {'posts': posts})

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'posts/detalle.html', {'post': post})
