from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer, correct_answer = quiz.next_question()
    score, answer_outcome = quiz.check_answer(user_answer, correct_answer)
    quiz.print_update(score, answer_outcome, correct_answer)
