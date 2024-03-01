import random
class Problems:
    def __init__(self):
        self.user_answer = 0
        self.correct_answer = None
        self.QUESTION_POOL = 1

    def getQuestion(self):
        pass
    def perimeterOfASquare(self):
        side_length = random.randint(0, 24)
        perimeterProblem = f"""
              The following is a square, and one
              of the sides is equal to {side_length}.

              Find the perimeter of the square.
                ------------
                |          |
                |          |
                |          | {side_length}
                |          |
                ------------
              """
        self.correct_answer = 4 * side_length
        return perimeterProblem
    
    def checkIfCorrect(self):
        if (self.user_answer == self.correct_answer):
            return True
        elif (self.user_answer != self.correct_answer):
            return False
    
    def setAnswer(self):
        self.user_answer = float(input(">> "))

def main():
    problem = Problems()
    for problems in range(100):
        problem.getQuestion()
        problem.setAnswer()