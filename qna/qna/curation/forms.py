from django import forms
from django.forms import modelformset_factory
from .models import Answer, Question

AnswerFormSet = modelformset_factory(Answer, form=forms.ModelForm, fields=['answer_text', 'value', 'category'], extra=3)

class QnaForm(forms.ModelForm):
    answer_forms = AnswerFormSet(queryset=Answer.objects.none())

    class Meta:
        model = Question
        fields='__all__'
        labels = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.answer_forms = AnswerFormSet(queryset=self.instance.answer_q.all())
        else:
            self.answer_forms = AnswerFormSet(queryset=Answer.objects.none())
            print('sss')
            print(self.answer_forms)

    def save(self, commit=True):
        question = super().save(commit=commit)
        if commit:
            answers_data = []
            for form in self.answer_forms:
                answer = form.save(commit=False)
                answer.question = question
                answer.save()
                form_data = form.cleaned_data
                answer_data = {
                    'answer_text': form_data.get('answer_text'),
                    'value': form_data.get('value'),
                    'category': form_data.get('category')
                }
                answers_data.append(answer_data)
            self.cleaned_data['answer_forms'] = answers_data
            self.answer_forms.save(commit=commit)
        return question




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


