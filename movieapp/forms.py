from django import forms
from.models import MovieList


class MovieForm(forms.ModelForm):
    class Meta:
        model=MovieList
        fields=['name','desc','Year','image']