from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def reciente(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=10)
    reciente.short_description = 'Recientemente publicado'
    reciente.boolean = True
    reciente.admin_order_field = 'pub-date'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question.question_text + '\n' + self.choice_text

    
