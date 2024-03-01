class Problems:
    def __init__(self):
        self.user_answer = 0
        self.correct_answer = None

    def getQuestion(self):
        pass
    def setAnswer(self):
        self.user_answer = float(input(">> "))

def main():
    problem = Problems()
    for problems in range(100):
        problem.getQuestion()
        problem.setAnswer()