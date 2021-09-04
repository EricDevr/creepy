from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from home.models import Posts
from .models import Comments
from .forms import CommentForm
# Create your views here.
def post(request, idu, titleu):
    postg = Posts.objects.get(id=idu)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        com = Comments()
        com.post = idu
        com.user = comment.data["user"]
        com.comment = comment.data["comment"]
        if comment.is_valid():
            com.save()
    form = CommentForm()
    comments = Comments.objects.filter(post=idu).order_by("-id")
    context = {
        'post': postg,
        'comments': comments,
        'form': form
    }
    return render(request, 'post.html', context)
def voto(request, id_post, voto):
    post = Posts.objects.get(id=id_post)
    if voto == 'like':
        post.like = post.like + 1
        post.save()
        json = {
            'cant': post.like,
            'voto': voto
        }
        return JsonResponse(json)
    else:
        post.dislike = post.dislike + 1
        post.save()
        json = {
            'cant': post.dislike,
            'voto': voto
        }
        return JsonResponse(json)