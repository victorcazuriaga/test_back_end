from django import forms


class ArchiveForm(forms.Form):
    data = forms.FileField()
