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
    current_question, current_answer = quiz.fetch_question_and_answer()
    user_answer = quiz.ask_question(current_question)
    score, answer_outcome = quiz.check_answer(user_answer, current_answer)
    quiz.print_update(score, answer_outcome, current_answer)
