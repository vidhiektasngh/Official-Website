from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'course', 'college', 'responsibility', 'phone_number', 'email', 'photo']