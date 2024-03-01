import random
class Problems:
    def __init__(self, cycles):
        self.cycles          = cycles
        self.user_answer     = None
        self.correct_answer  = None
        self.correct_answers = 0

    def getQuestion(self):
        self.user_answer    = None
        self.correct_answer = None
        self.displayCurrentScore()
        self.perimeterOfASquare()

    def setAnswer(self):
        self.user_answer = input(">> ")
        self.user_answer = int(self.user_answer)
    
    def checkIfUserIsCorrect(self):
        if (self.user_answer == self.correct_answer):
            self.correct_answers += 1

    def displayCurrentScore(self):
        print(f"\t\t\tcorrect answers [{self.correct_answers}/{self.cycles}]")

    def findQuestion(self, random_value):
        match random_value:
            case 0:
                self.perimeterOfASquare()
            case 1:
                self.areaOfASquare()

    def perimeterOfASquare(self):
        side_length = random.randint(0, 24)
        perimeterProblem = f"""
              
              The following is a square, and one
              of the sides is equal to {side_length}.

              Find the perimeter of the square.
                -----------------
                |  |         |  |
                |---         ---|
                |               | {side_length} 
                |__           __|
                |  |         |  |
                -----------------
              """
        self.correct_answer = 4 * side_length
        print(perimeterProblem)
    
    def areaOfASquare(self):
        side_length = random.randint(0, 10)
        areaProblem = f"""

              The following is a square, and one
              of the sides is equal to {side_length}.

              Find the area of the square.
                -----------------
                |  |         |  |
                |---         ---|
                |               | 
                |__           __|
                |  |         |  |
                -----------------
                        {side_length} 
        """
        self.correct_answer = pow(side_length, 2)
        print(areaProblem)

def main():
    problem = Problems(100)
    for problems in range(problem.cycles):
        problem.getQuestion()
        problem.setAnswer()
        problem.checkIfUserIsCorrect()
main()