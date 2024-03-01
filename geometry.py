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

def main():
    problem = Problems(100)
    for problems in range(problem.cycles):
        problem.getQuestion()
        problem.setAnswer()
main()