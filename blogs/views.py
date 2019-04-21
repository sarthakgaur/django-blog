from django.shortcuts import render
from .models import BlogPost
from .forms import BlogForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    """Render the home page."""
    return render(request, 'blogs/home.html')

def posts(request):
    """Render the posts page."""
    posts = BlogPost.objects.order_by('-date')
    content = {'posts': posts}
    return render(request, 'blogs/posts.html', content)

@login_required
def new_post(request):
    """Render the new request page."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    
    content = {'form': form}
    return render(request, 'blogs/new_post.html', content)

@login_required
def edit_post(request, post_id):
    """Render the edit_post page."""
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = BlogForm(instance=post)
        else:
            form = BlogForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('blogs:posts'))
        
    content = {'form': form, 'post_id': post_id}
    return render(request, 'blogs/edit_post.html', content)