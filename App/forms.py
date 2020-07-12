from django import forms
from django.forms import SelectDateWidget

from App.models import CourseModel,StudentModel

class CourseForm(forms.ModelForm):
    date=forms.DateField(widget=SelectDateWidget)
    time=forms.TimeField(widget=forms.DateTimeInput(attrs={'type':'time'}))
    class Meta:
        model=CourseModel
        fields='__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
