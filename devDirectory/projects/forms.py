from django.forms import ModelForm
from django import forms
from .models import Project,Review,Post




class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['caption','image']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demo_link','source_link']
        widgets = {
            'tags':forms.CheckboxSelectMultiple()
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
        'value' : 'Place your vote',
        'body'  : 'Write a review'
        }

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
