
from django import forms

from core.models import Post


class PostForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = ['title','visibility','images']
        
        
    def save(self,commit=True):
        post= super().save(commit=False)
        if commit:
            post.save()
        return post
