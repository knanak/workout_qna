from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'curation/main.html')

def neck(request):
    return render(request, 'curation/neck.html')

def shoulder(request):
    return render(request, 'curation/shoulder.html')

def back(request):
    return render(request, 'curation/back.html')


def hip(request):
    return render(request, 'curation/hip.html')


def knee(request):
    return render(request, 'curation/knee.html')
