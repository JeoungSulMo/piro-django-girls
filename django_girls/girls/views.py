from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Cat
# Create your views here.


def post_list(request):
    posts = Cat.objects.all()
    #posts = Cat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'girls/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts=get_object_or_404(Cat, pk=pk)
    return render(request,'girls/post_detail.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'girls/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Cat, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'girls/post_edit.html', {'form': form})