from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.forms import formset_factory
from django.core.cache import cache
from . import models, serializers, forms
import json, copy


selected=[]
answer=[]
first, endPont=5, 11

def edit(request, q_id):
    if request.user.is_authenticated:
        question=models.Question.objects.get(id=q_id)
        AnswerFormSet = formset_factory(forms.AnswerForm, extra=0)
        
        if request.user != question.author :
            return redirect(reverse('curation:main'))

        if request.method == 'GET':
            form=forms.EditQnaForm(instance=question)
            answers = models.Answer.objects.filter(question=question).order_by('id')

            initial_data = []
            for answer in answers:
                initial_data.append({
                    'answer_text': answer.answer_text,
                    'value': answer.value,
                    'category': answer.category
                })

            formset = AnswerFormSet(initial=initial_data)
            return render(request, 'curation/edit.html', {'form': form, 'formset': formset, 'question':question})
        
        elif request.method == 'POST':
            
            form=forms.EditQnaForm(request.POST)
            formset=AnswerFormSet(request.POST)
            answers = models.Answer.objects.filter(question=question).order_by('id')

            if form.is_valid() and formset.is_valid():
                question.question_text=form.cleaned_data['question_text']
                question.save()

                for i in range(len(answers)):
                    answer=answers[i]
                    answer.answer_text=formset[i].cleaned_data['answer_text']
                    answer.value=formset[i].cleaned_data['value']
                    answer.category=formset[i].cleaned_data['category']
                    answer.save()
            
                return redirect(reverse('curation:manage'))

            else:
                print('not valid form')
                
    return render(request, 'curation/list.html')

def list(request, q_id):
    if request.user.is_authenticated:
        ## if request.user == author 일치하면
        q = models.Question.objects.get(id=q_id)
        q_s=serializer = serializers.QnaSerializer(q)

        questions = models.Question.objects.filter(id__range=(q_id, q_id + 6)).order_by("id")
       
        question_data = []
        for question in questions:
            serializer = serializers.QnaSerializer(question)
            question_data.append({
                'question': serializer.data,
                'answers': question.answer_q.all()[:3]  # 역참조
            })

        return render(request, 'curation/list.html', {'q_s':q_s, 'question_data': question_data})


        if request.method == 'GET':
            form=forms.QnaForm(instance=questions)
            return render(request, 'curation/list.html', {"form":form, "questions":questions})


def manage(request):
    if request.user.is_authenticated:
        if not request.user.user_type.userType == 'customer':
            questions = models.Question.objects.all().order_by("create")
            serializer = serializers.QnaSerializer(questions, many=True)
            return render(request, 'curation/manage.html', {'data':serializer.data})
          

cnt = 0
qList=[]
aList=[]                                                                                          
def register(request):   
    global cnt,qList,aList
    AnswerFormSet = formset_factory(forms.AnswerForm, extra=3)

    if request.method == 'GET':
        cnt=0
        qList=[]
        aList=[] 
        form = forms.QnaForm()
        formset = AnswerFormSet()
        return render(request, 'curation/register.html', {'form': form, 'formset': formset})
    
    elif request.method == 'POST':
        form = forms.QnaForm(request.POST)
        formset = AnswerFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # print(request.POST['q_index'])
            parent = form.save(commit=False)
            qList.append(parent)
            # parent.save()
            

            for form2 in formset:
                child = form2.save(commit=False)
                child.question = parent
                aList.append(child)
                # child.save()
            cnt+=1
            print(cnt)

            # 이전 입력값 지워주기
            form = forms.QnaForm(initial={'question_category': form.cleaned_data['question_category'],
                                          'question_title':form.cleaned_data['question_title']})
            # formset = AnswerFormSet()

            # form.save()한 뒤에 form.cleaned_data['칼럼명']을 reverse()로 전달하여 질문 카테고리에 따라 동적으로 redirect 페이지를 변경
            question_category=form.cleaned_data['question_category']

            if cnt == 2 :
                for q in qList:
                    q.save()

                for a in aList:
                    a.save()

                url = reverse(f'curation:{question_category}')
                cnt=0 # 질문 갯수를 채우면, 다시 카운트를 0으로 돌려줘야
                return HttpResponseRedirect(url)
                        
            return render(request, 'curation/register.html', {'form': form, 'formset': formset})
        
        else:
            print('not valid form')
            return render(request, 'curation/register.html', {'form': form, 'formset': formset})



def main(request):
    return render(request, 'curation/main.html')

def neck(request):
    question=models.Question.objects.filter(question_category__name__iexact='neck').first()
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/neck.html', {'data':serializer.data})

def shoulder(request):
    question=models.Question.objects.filter(question_category__name__iexact='shoulder').first()
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/shoulder.html', {'data':serializer.data})

def back(request):
    question=models.Question.objects.filter(question_category__name__iexact='back').first()
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/back.html', {'data':serializer.data})


def hip(request):
    question=models.Question.objects.filter(question_category__name__iexact='hip').first()
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/hip.html', {'data':serializer.data})


def knee(request):
    question=models.Question.objects.filter(question_category__name__iexact='knee').first()
    serializer = serializers.QnaSerializer(question)
    return render(request, 'curation/knee.html', {'data':serializer.data})

def getQna(request, q_name, q_id):
    if request.method == 'GET':

        # question=get_object_or_404(models.Question, pk=1)
        # question=models.Question.objects.get(id=q_id)
        # serializer = serializers.QnaSerializer(question)
        # return render(request, 'curation/qna.html', {"question":serializer.data})
        if q_id % 7 == 5:
            if 'first' not in request.session: 
                request.session['first'] = 'first'
                question = models.Question.objects.get(question_category__name__iexact=q_name, id=q_id)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            else :
                del request.session['first']
                question = models.Question.objects.get(question_category__name__iexact=q_name, id=q_id+1)
                serializer = serializers.QnaSerializer(question)
                return render(request, 'curation/qna.html', {"question":serializer.data})
            
        elif q_id % 7 == 4:
            if 'first' in request.session: 
                del request.session['first']
            return redirect(reverse('curation:result'))
        
        else :
            if 'first' in request.session: 
                del request.session['first']
            question = models.Question.objects.get(question_category__name__iexact=q_name, id=q_id+1)
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
    print(selected)
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
    print(pointer)
    answer_result=models.Result.objects.get(category=pointer)
    serializer = serializers.ResultSerializer(answer_result)
    
    return render(request, 'curation/result.html', {'result':serializer.data})
