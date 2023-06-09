from django.db import models
from qna.users import models as user_model

class TimeStamp(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True
    

class QuestionCategory(TimeStamp):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class AnswerCategory(TimeStamp):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Question(TimeStamp):
    author=models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='autor_q', null=True)
    question_title = models.CharField(max_length=300, null=True)
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.question_text


class Answer(TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answer_q')
    answer_text = models.CharField(max_length=400, null=True)
    value=models.IntegerField(default=0, null=True)
    category = models.ForeignKey(AnswerCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.answer_text:
            return self.answer_text
        else:
            return "No answer provided"


class Result(TimeStamp):
    name = models.CharField(max_length=500, null=True)
    desc = models.CharField(max_length=2000, null=True)
    youtube = models.URLField("URL", null=True)
    category = models.ForeignKey(AnswerCategory, on_delete=models.CASCADE, null=True, related_name='result_category')
    vaule=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name