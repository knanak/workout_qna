from rest_framework import serializers
from. import models

class QnaCategorySerializer(serializers.ModelSerializer):
    class Meta :
        model=models.QuestionCategory
        fields=("id", "name")

class AnswerCategorySerializer(serializers.ModelSerializer):
    class Meta :
        model=models.AnswerCategory
        fields=("id", "name")


class AnswerSerializer(serializers.ModelSerializer):
    category = AnswerCategorySerializer()
    class Meta :
        model=models.Answer
        fields='__all__'
        

class QnaSerializer(serializers.ModelSerializer):
    question_category = QnaCategorySerializer()
    answer_q = AnswerSerializer(many=True)
    
    class Meta :
        model=models.Question
        fields=("id", "question_category", "question_text", "answer_q")


class ResultSerializer(serializers.ModelSerializer):
    category = AnswerCategorySerializer()
    class Meta :
        model=models.Result
        fields=("id", "name", "desc", "category", "youtube")