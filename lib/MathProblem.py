#/usr/bin/env python3

import re
from lib.Problem import Problem

class MathProblem(Problem):
    __solution = ""
    __hint = ""

    def __init__(self,question="",answer="",solution="",hint=""):
        self.solution = solution
        self.hint = hint
        Problem.__init__(self,question,answer)
        self.type = "MathProblem"

    def check_answer(self,a):
        return (self.answer == a) 

    def set_hint(self, hint):
        self.hint = hint

    def set_solution(self,solution):
        self.solution = solution

    def get_hint(self):
        return self.hint

    def get_solution(self):
        return self.solution

    def as_string(self):
        return "MathProblem|{}|{}|{}|{}|".format(self.question,self.answer,self.solution,self.hint)

    def copy(self):
        return MathProblem(self.question,self.answer,self.solution,self.hint)

if __name__ == "__main__": test()
