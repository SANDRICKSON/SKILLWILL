from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

from django.db.models import Q

def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # წაშალე ეს ნაწილი:
            # if request.user.is_authenticated:
            #     post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # ეს მხოლოდ მაშინ უნდა მოხდეს, როცა ავტორიზებული მომხმარებელი არ არის
    if request.user.is_authenticated:
        # თუ მომხმარებელი არ არის ავტორიზებული, უნდა წაშალოს ან დაემატოს
        if post.author != request.user:
            return redirect('post_list')  # აქ უნდა წასულიყო მხოლოდ პოსტის ავტორს რედაქტირება

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def profile_view(request, username):
    posts = Post.objects.filter(post_author=username)
    return render(request, 'posts/profile.html', {'username': username, 'posts': posts})


def post_search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})