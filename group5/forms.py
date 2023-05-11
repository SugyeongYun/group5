from django import forms
from group5.models import Question, Preference


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'message']


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['date', 'person_cnt', 'price']