from django import forms
from . models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']

class Free_course_applyForm(forms.ModelForm):
    class Meta:
        model = Free_course_apply
        fields = ['name', 'email', 'phone', 'message']

class Blog_replyForm(forms.ModelForm):
    class Meta:
        model= Blog_reply
        fields=['name', 'email', 'website', 'message']
