from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from. import models, serializers
import json, copy
from operator import itemgetter
selected=[]
answer=[]

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
            if 'first' not in request.session: 
                request.session['first'] = 'first'
                question=get_object_or_404(models.Question, pk=q_id)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            else :
                del request.session['first']
                question=get_object_or_404(models.Question, pk=q_id+1)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            
        elif q_id==endPont:
            return redirect(reverse('curation:result'))
        
        else :
            question=get_object_or_404(models.Question, pk=q_id+1)
            serializer = serializers.QnaSerializer(question)
            return render(request, 'curation/qna.html', {"question":serializer.data})


    elif request.method == 'POST':
        response_body = {"q": "", "a": [], "q_id":""}
        # question=models.Question.objects.get(id=q_id+1)
        # response_body['q'] = question.question_text
        # response_body['q_id'] = question.id

        # answers = question.answer_q.all()
        # for answer in answers:
        #     response_body['a'].append({
        #     'id': answer.id,
        #     'text': answer.answer_text,
        #     'category': answer.category.name,
        #     'value':answer.value,
        # })
        data = json.loads(request.body.decode('utf-8'))
        selected.append(data)

        return JsonResponse(status=200, data=response_body)
    


def result(request):
    # 최고값인 category를 전달 받아 resultSerializer로 html에 전달해주기
    point={}
     
    global selected
    answer=copy.deepcopy(selected)
    selected=[]

    for a_id in answer:
        a=models.Answer.objects.get(id=a_id)
        if a.category in point :
            point[a.category]+=a.value
        else :
            point[a.category]=a.value

    point=sorted(point.items(), key=lambda x: x[1])
 
    pointer=point[-1][0]
    answer_result=models.Result.objects.get(category=pointer)
    serializer = serializers.ResultSerializer(answer_result)
    
    return render(request, 'curation/result.html', {'result':serializer.data})


