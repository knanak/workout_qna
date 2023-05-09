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
        fields=("id", "question", "answer_text", "category")


class QnaSerializer(serializers.ModelSerializer):
    answer_q = AnswerSerializer(many=True)
    class Meta :
        model=models.Question
        fields=("id", "question_text", "answer_q")

