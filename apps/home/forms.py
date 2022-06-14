from django import forms

class RefusForm(forms.Form):
    motif = forms.CharField(widget=forms.Textarea, required=True)