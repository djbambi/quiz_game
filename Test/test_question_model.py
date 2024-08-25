from question_model import Question

def test_field_access():
    q = Question("Text", "Answer")
    assert q.text == "Text"
    assert q.answer == "Answer"