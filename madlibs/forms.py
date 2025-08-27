from django import forms

class DynamicMadLibForm(forms.Form):
    def __init__(self, fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in fields:
            self.fields[field] = forms.CharField(
                label=field.replace('_', ' ').title(),
                widget=forms.TextInput(attrs={'class': 'form-control shadow'}),
                required=True
            )
