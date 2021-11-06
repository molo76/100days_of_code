class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}, {question.text} (True or False)?: ")
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.user_score += 1
        else:
            print("You were wrong")
        print(f"The correct answer was '{correct_answer}'")
        print(f"Current score is {str(self.user_score)} out of {self.question_number}\n\n")
