from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from. import models, serializers
first=5
endPont=11

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
        # question=get_object_or_404(models.Question, pk=1)
        # question=models.Question.objects.get(id=q_id)
        # serializer = serializers.QnaSerializer(question)
        # return render(request, 'curation/qna.html', {"question":serializer.data})
        if q_id==5:
            if 'aa' not in request.session: 
                request.session['aa'] = 'first'
                question=get_object_or_404(models.Question, pk=q_id)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            else :
                del request.session['aa']
                question=get_object_or_404(models.Question, pk=q_id+1)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            
        elif q_id==endPont:
            # 선택한 답 저장하여 계산하고 result로 넘겨주기
            # result=get_object_or_404(models.Result, pk=2)
            # serializer = serializers.QnaSerializer(result)
            return redirect(reverse('curation:result'))
        
        else :
            question=get_object_or_404(models.Question, pk=q_id+1)
            serializer = serializers.QnaSerializer(question)
            return render(request, 'curation/qna.html', {"question":serializer.data})


    elif request.method == 'POST':
        response_body = {"q": "", "a": [], "q_id":""}
        question=models.Question.objects.get(id=q_id+1)
        response_body['q'] = question.question_text
        response_body['q_id'] = question.id

        answers = question.answer_q.all()
        for answer in answers:
            response_body['a'].append({
            'id': answer.id,
            'text': answer.answer_text,
            'category': answer.category.name,
            'value':answer.value,
        })
        return JsonResponse(status=200, data=response_body)
    


def result(request): # 최고값인 category를 전달 받아 resultSerializer로 html에 전달해주기
    return render(request, 'curation/result.html')

def nextQna(request, q_id):
    response_body = {"q": "", "answers": []}
    question = get_object_or_404(models.Question, pk=q_id)
    response_body['q'] = question.id
    answers = question.answer_q.all()
    for answer in answers:
        response_body['answers'].append({
            'id': answer.id,
            'text': answer.answer_text,
            'category': answer.category.name,
            'value':answer.value,
        })

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
