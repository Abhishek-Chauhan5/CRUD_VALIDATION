from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        
    
    # ADD VALIDATION FOR NAME FIELD
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Age should be at least 18.")
        
        if age >60:
            raise forms.ValidationError("Age should not be greater than 60.")    
        return age