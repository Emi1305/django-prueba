from urllib import request

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    from .models import Question
    #template = loader.get_template('polls/index.html')
    preguntas = Question.objects.order_by('-pub_date')
    #response = '<br>'.join([p.question_text for p in preguntas])
    #return HttpResponse('Hello world. This is the polls index<br><br>' + response)
    context = {'preguntas': preguntas}
    #return HttpResponse(template.render(context=context, request=request))
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    from .models import Question
    pregunta = get_object_or_404(Question, pk=question_id)
    context = {'pregunta': pregunta}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    from .models import Question, Choice
    pregunta = get_object_or_404(Question, pk=question_id)
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'pregunta':pregunta, 'error_message':'No selecciono ningun opcion.'})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    from .models import Question, Choice
    pregunta = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'pregunta': pregunta})