from django.db import models

class TimeStamp(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True
    
class Question(TimeStamp):
    contents = models.TextField(max_length=500)

class Answer(TimeStamp):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_question')
    a1 = models.TextField(max_length=700)
    a2 = models.TextField(max_length=700)
    a3 = models.TextField(max_length=700)