from rest_framework import serializers
from. import models

class QnaSerializer(serializers.ModelSerializer):
    class Meta :
        model=models.Question
        fields=("id", "contents")

class AnswerSerializer(serializers.ModelSerializer):
    class Meta :
        model=models.Answer
        fields=("id", "a1", "a2", "a3")