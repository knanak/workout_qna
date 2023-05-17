from django.db import models

class TimeStamp(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True
    
class Category(TimeStamp):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Question(TimeStamp):
    question_text = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.question_text


class Answer(TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answer_q')
    answer_text = models.CharField(max_length=400, null=True)
    value=models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.answer_text
    

class Result(TimeStamp):
    name = models.CharField(max_length=500, null=True)
    desc = models.CharField(max_length=2000, null=True)
    youtube = models.URLField("URL", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='result_category')
    vaule=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name