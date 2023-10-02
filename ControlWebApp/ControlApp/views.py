from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'ControlApp/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'ControlApp/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'ControlApp/post_new.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'ControlApp/post_edit.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('post_list')

def comment_edit(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('post_detail', id=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'ControlApp/comment_edit.html', {'form': form})

def comment_delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', id=post_pk)

def comment_new(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=id)
    else:
        form = CommentForm()
    return render(request, 'ControlApp/comment_new.html', {'form': form})