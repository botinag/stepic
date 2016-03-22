from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from qa.models import Question, Answer


class AskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AskForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AskForm, self).save(commit=False)
        if not self.user.is_anonymous():
            instance.author = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Question
        fields = ('title', 'text')


class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AnswerForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AnswerForm, self).save(commit=False)
        if not self.user.is_anonymous():
            instance.author = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Answer
        fields = ('text', 'question')
        widgets = {'question': forms.HiddenInput()}


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
