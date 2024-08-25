from quiz_brain import QuizBrain
from unittest.mock import patch

# Define the MockQuestion class here if used in multiple tests


class MockQuestion:
    def __init__(self, text):
        self.text = text


def test_field_access():
    question_list = ['q1', 'q2']
    q = QuizBrain(question_list)
    assert q.question_number == 0
    assert q.question_list == question_list


def test_question_number_increments():
    question_list = [MockQuestion("Question 1"), MockQuestion("Question 2")]
    quiz = QuizBrain(question_list)

    with patch('builtins.input', return_value="True"):
        quiz.next_question()

    assert quiz.question_number == 1
