from django.views import generic
from .models import *
from django.shortcuts import render


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     # model = Post
#     template_name = 'post_detail.html'

def post(requet):
    posts=Post.objects.filter(status=1).order_by('-created_on')
    return render(requet,'index.html',{'posts':posts})


def show_post(requet,id):
    id=int(id)
    post=Post.objects.get(pk=id)
    exercice=Exercices.objects.filter(exercice_post=id)
    return render(requet,'post_detail.html',{'post':post,'exos':exercice})

    
