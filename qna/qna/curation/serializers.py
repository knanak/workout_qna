from rest_framework import serializers
from. import models
from qna.users.models import User 

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

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id", "name")
        

class QnaSerializer(serializers.ModelSerializer):
    question_category = QnaCategorySerializer()
    answer_q = AnswerSerializer(many=True)
    author = AuthorSerializer()
    
    class Meta :
        model=models.Question
        fields=("id", "question_category", "question_title", 'author', "question_text", "answer_q")


class ResultSerializer(serializers.ModelSerializer):
    category = AnswerCategorySerializer()
    class Meta :
        model=models.Result
        fields=("id", "name", "desc", "category", "youtube")