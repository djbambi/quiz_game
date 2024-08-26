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


def test_correct_question_selected():
    # Arrange
    question_list = [MockQuestion("Question 1"), MockQuestion("Question 2")]
    quiz = QuizBrain(question_list)

    # Act
    with patch('builtins.input', return_value="True"):  # Mock the input function
        quiz.next_question()

    # Assert
    assert quiz.question_list[quiz.question_number - 1].text == "Question 1"


def test_still_has_questions_returns_true():
    question_list = [MockQuestion("Question 1"), MockQuestion("Question 2")]
    quiz = QuizBrain(question_list)

    assert quiz.still_has_questions() == True
