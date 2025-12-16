# blog/forms.py
from django import forms
from .models import Post, Category, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Post Content'}),
            'category': forms.Select(),
            'tags': forms.CheckboxSelectMultiple(),
            'status': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make category/tags optional and sort for a nicer dropdown/checkbox list
        self.fields['category'].required = False
        self.fields['tags'].required = False
        self.fields['category'].queryset = Category.objects.order_by('name')
        self.fields['tags'].queryset = Tag.objects.order_by('name')
        # Friendly empty label for category dropdown
        self.fields['category'].empty_label = 'No category'
