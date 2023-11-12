from django.db import models


class CorrectAnswer(models.TextChoices):
    A = "A", "A answer"
    B = "B", "B answer"
    C = "C", "C answer"
    D = "D", "D answer"


class QuestionLevel(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Question(models.Model):
    question = models.TextField()
    a_answer = models.TextField()
    b_answer = models.TextField()
    c_answer = models.TextField()
    d_answer = models.TextField()
    correct_answer = models.CharField(
        max_length=1, choices=CorrectAnswer.choices)
    level = models.IntegerField(
        choices=QuestionLevel.choices, default=QuestionLevel.LOW)

    def __str__(self):
        return self.question
