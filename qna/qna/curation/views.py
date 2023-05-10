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
    # question=get_object_or_404(models.Question)
    # serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/back.html')


def hip(request):
    return render(request, 'curation/hip.html')


def knee(request):
    return render(request, 'curation/knee.html')

def getQna(request, q_id):
    if request.method == 'GET':
        question=get_object_or_404(models.Question, pk=q_id)
        serializer = serializers.QnaSerializer(question)
        return render(request, 'curation/qna.html', {"question":serializer.data})
    
    elif request.method == 'POST':
        response_body = {"q": "", "answers": []}
        question=get_object_or_404(models.Question, pk=q_id+3)
        response_body['q'] = question.question_text
        answers = question.answer_q.all()
        for answer in answers:
            response_body['answers'].append({
            'id': answer.id,
            'text': answer.answer_text,
            'category': answer.category.name
        })
        print(response_body['answers'][1]['text'])
        return JsonResponse(status=200, data=response_body)
    


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


def get_next_question(request, current_question_id):
    current_question = models.Question.objects.get(id=current_question_id)
    next_question = models.Question.objects.filter(id__gt=current_question_id).first()

    if next_question is None:
        # We've reached the end of the questions
        return JsonResponse({'status': 'end'})
    
    next_answer = models.Answer.objects.filter(question=next_question).first()
    return JsonResponse({
        'status': 'ok',
        'next_question': next_question.question_text,
        'next_answer': next_answer.answer_text,
        'next_question_id': next_question.id,
    })
