from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from. import models, serializers

# Create your views here.
def main(request):
    return render(request, 'curation/main.html')

def neck(request):
    return render(request, 'curation/neck.html')

def shoulder(request):
    return render(request, 'curation/shoulder.html')

def back(request):
    question=get_object_or_404(models.Question)
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/back.html', {"serializer":serializer.data})


def hip(request):
    return render(request, 'curation/hip.html')


def knee(request):
    return render(request, 'curation/knee.html')

def getQna(request):
    question=get_object_or_404(models.Question)
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/qna.html', {"question":serializer.data})


def nextQna(request, q_id):
    reponse_body={"q":""}
    question=get_object_or_404(models.Question, pk=q_id)
    reponse_body['q']=question.question_text
    # answer=get_object_or_404(models.Answer)


    # for i in answer :
    #     reponse_body[f'a{i.id}']=i.answer_text
    return JsonResponse(status=200, data=reponse_body)
