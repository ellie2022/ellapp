from django import forms
from ellapp.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question    # model to be used
        fields = ['subject', 'content'] # attributes of the model to be used in QuestionForm
        labels = {
            'subject': 'Subject',
            'content': 'Detail',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'Your Answer'
        }