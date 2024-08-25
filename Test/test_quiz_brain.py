from quiz_brain import QuizBrain


def test_field_access():
    question_list = ['q1', 'q2']
    q = QuizBrain(question_list)
    assert q.question_number == 0
    assert q.question_list == question_list
