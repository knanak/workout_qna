from rest_framework import serializers
from. import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model=models.Category
        fields=("id", "name")


class AnswerSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta :
        model=models.Answer
        fields='__all__'
        


class QnaSerializer(serializers.ModelSerializer):
    answer_q = AnswerSerializer(many=True)
    class Meta :
        model=models.Question
        fields=("id", "question_text", "answer_q")

class ResultSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta :
        model=models.Result
        fields=("id", "name", "desc", "category", "youtube")