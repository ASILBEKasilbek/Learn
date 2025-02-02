from django import forms

class AnswerForm(forms.Form):
    user_answer = forms.CharField(widget=forms.Textarea, required=True)
