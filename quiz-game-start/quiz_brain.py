class QuizBrain:
# --------------------- initialize (constractor)the class -------------------- #
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                              Methods Definitions                             #
# ---------------------------------------------------------------------------- #
# ----------- check if there is still a question in the list or not ---------- #
    def still_has_a_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
# ---------------------------------------------------------------------------- #
# -------------------- Go to the next qustion in the list -------------------- #
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number} {current_question.text}.(True|False)?: ")
        correct_answer=current_question.answer
        self.check_answer(user_answer,correct_answer)
# ---------------------------------------------------------------------------- #
    def check_answer(self,user_answer,correct_answer,):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it Right!")
        else:
            print("That is Wrong")
        print(f"the correct Answer is: {correct_answer} .")
        print(f"you current score is {self.score}/{self.question_number}")
        print("\n")
# ---------------------------------------------------------------------------- #