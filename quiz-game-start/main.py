from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


question = QuizBrain(question_bank)
while question.still_has_questions():
    question.next_question()

print("You have complated the quiz.")
print(f"Your final score was: {question.score}/{question.question_number}")