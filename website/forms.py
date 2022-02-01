from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Seu nome', max_length=100)
    contact = forms.CharField(label='Email ou telefone (opcional)', max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea, label='Sua mensagem', max_length=600)


