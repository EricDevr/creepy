from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def createPost(request):
    message = ""
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message = "aregado"
            form = PostForm()
    else:
        form = PostForm()
    context = {
        'message': message,
        'form': form,
    }
    return render(request, 'createpost.html', context)