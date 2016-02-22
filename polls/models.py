from __future__ import unicode_literals
import datetime
from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def test_was_published_recently_with_old_question(self):
#was_published_recently() debe devolver False de preguntas cuyo pub_date es mas de 1dia.
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
#was_published_recently() debe devolver True para preguntas cuyo pub_date esta dentro del ultimo dia.
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)

    """
  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    """
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
