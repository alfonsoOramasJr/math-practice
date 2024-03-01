class Problems:
    def __init__(self):
        self.answer = 0

    def getQuestion(self):
        pass
    def setAnswer(self):
        self.answer = float(input(">> "))

def main():
    problem = Problems()
    for problems in range(100):
        problem.getQuestion()
        problem.setAnswer()