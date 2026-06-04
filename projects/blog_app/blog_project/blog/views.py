

# Create your views here.
from django.shortcuts import render
from .models import Post

def home(request):
    return render(
        request,
        "home.html"
    )

def home(request):

    posts = Post.objects.all()

    return render(
        request,
        'home.html',
        {
            'posts': posts
        }
    )

def post_detail(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    return render(
        request,
        'detail.html',
        {
            'post': post
        }
    )