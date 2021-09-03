from django.http.response import JsonResponse
from django.shortcuts import render
from home.models import Posts
# Create your views here.
def post(request, idu, titleu):
    postg = Posts.objects.get(id=idu)
    context = {
        'post': postg,
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