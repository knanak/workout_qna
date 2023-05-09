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
    if request.method == 'GET':
        question=get_object_or_404(models.Question)
        serializer = serializers.QnaSerializer(question)
        return render(request, 'curation/qna.html', {"question":serializer.data})


def nextQna(request, q_id):
    response_body = {"q": "", "answers": []}
    question = get_object_or_404(models.Question, pk=q_id)
    response_body['q'] = question.id
    answers = question.answer_q.all()
    for answer in answers:
        response_body['answers'].append({
            'id': answer.id,
            'text': answer.answer_text,
            'category': answer.category.name
        })
    print(response_body['answers'][1]['id'])
    return JsonResponse(status=200, data=response_body)
