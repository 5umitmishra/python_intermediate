from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question_text = key["text"]
    question_answer = key["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
