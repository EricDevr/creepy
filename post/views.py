from django.shortcuts import render
from home.models import Posts
# Create your views here.
def post(request, idu, titleu):
    postg = Posts.objects.get(id=idu)
    context = {
        'post': postg,
    }
    return render(request, 'post.html', context)