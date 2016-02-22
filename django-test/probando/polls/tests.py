from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question
# Create your tests here.


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.reciente(), False)

    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=50)
        past_question = Question(pub_date=time)
        self.assertEqual(past_question.reciente(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.reciente(), True)