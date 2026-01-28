from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_home(request):
    all_posts = Post.objects.all().order_by('-created_at')
    
    paginator = Paginator(all_posts, 5) 
    
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})
