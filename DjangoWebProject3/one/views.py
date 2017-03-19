from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by()[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def search(request):
    if 'q' in request.GET:

        b=Question(question_text=request.GET['q'])
        b.save()
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    #coise = get_object_or_404(Choice,pk = question_id)
    return render(request, 'detail.html', {'question': question})

def addcom(request):

    return HttpResponse("пока не работает")



# Create your views here.
#  176.195.247.216:
#http://176.195.247.216:8000/one/
# python manage.py runserver 176.195.247.216:8000