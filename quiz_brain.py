class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def fetch_question_and_answer(self) -> tuple[str, str]:
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        return current_question, correct_answer

    def ask_question(self, current_question) -> str:
        user_answer = input(
            f'Q.{self.question_number}: {current_question.text} (True/False): ')
        return user_answer

    def check_answer(self, user_answer, correct_answer) -> int:
        if user_answer == correct_answer:
            self.score += 1
            return self.score, True
        return self.score, False

    def print_update(self, score, answer_outcome, correct_answer) -> None:
        if answer_outcome:
            print('You got it right!')
        else:
            print('You got it wrong!')
        print(f'The correct answer is: {correct_answer}')
        print(f'Your current score is: {score}/{self.question_number}\n')
