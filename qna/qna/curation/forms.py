from django import forms
from django.forms import modelformset_factory
from .models import Answer, Question

class EditQnaForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = Question
        fields=['question_text']
        labels = {}



class QnaForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question_category', 'question_title', 'question_text']
        labels = {}

    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields=['answer_text', 'value', 'category']
        labels = {}

    

    # def save(self, commit=True):
    #     question = super().save(commit=commit)
    #     if commit:
    #         for answer_form in self.answer_forms:
    #             answer = answer_form.save(commit=False)
    #             answer.question = question
    #             answer.save()
    #         self.answer_forms.is_valid()  # Call is_valid() on the formset to trigger the clean() method
    #         self.answer_forms.save()
    #     return question

