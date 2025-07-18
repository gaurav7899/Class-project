from django import forms
from main.models import logIn,register,course
class loginForm(forms.ModelForm):
    class Meta:
        model=logIn
        fields=["username","password"]
        

class registerForm(forms.ModelForm): 
    course = forms.ModelChoiceField(
        queryset=course.objects.all(),
        empty_label="Select a course",  # optional placeholder
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = register
        fields = "__all__"
