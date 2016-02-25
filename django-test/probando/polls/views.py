from urllib import request

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
# Create your views here.


# Con funciones:
# def index(request):
#
#     #template = loader.get_template('polls/index.html')
#     preguntas = Question.objects.order_by('-pub_date')
#     #response = '<br>'.join([p.question_text for p in preguntas])
#     #return HttpResponse('Hello world. This is the polls index<br><br>' + response)
#     context = {'preguntas': preguntas}
#     #return HttpResponse(template.render(context=context, request=request))
#     return render(request,'polls/index.html',context)
#
# def detail(request, question_id):
#
#     pregunta = get_object_or_404(Question, pk=question_id)
#     context = {'pregunta': pregunta}
#     return render(request, 'polls/detail.html', context)
#
#
# def results(request, question_id):
#
#     pregunta = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'pregunta': pregunta})


# Con clases genericas:
class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'preguntas'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())[:5]

class DetailView(generic.DetailView):

    template_name = 'polls/detail.html'
    model = Question
    context_object_name = 'pregunta'

class ResultsView(generic.DetailView):

    template_name = 'polls/results.html'
    model = Question
    context_object_name = 'pregunta'



def vote(request, question_id):

    pregunta = get_object_or_404(Question, pk=question_id)
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'pregunta':pregunta, 'error_message':'No selecciono ningun opcion.'})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))