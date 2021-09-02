from django import forms
from home.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('autor','image','title','content',)