from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})
