from django.conf.urls import url

from . import views

app_name = 'polls'
# Con funciones:
# urlpatterns = [
#     url(r'^$', views.index, name='index'), #/polls/
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'), #/polls/01/
#     url(r'^(?P<question_id>\d+)/result/$', views.results, name='results'), #/polls/01/result/
#     url(r'^(?P<question_id>\d+)/votes/$', views.vote, name='votes'), #/polls/01/votes/
# ]

# Con clases genericas:
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/votes/$', views.vote, name='votes'),
]