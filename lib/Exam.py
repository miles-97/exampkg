#!/usr/bin/env python3

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet

class Exam(ProblemSet):
    __points_per_problem = 0 #val > 0 if all problems have the same val
                             #val = 0 if problems have diff vals
    #__points_arr = []        #if each problem has a different point value

    def __init__(self,name="",points=0,problem_set=None):
        super(Exam,self).__init__(name)
        self.points_per_problem = points

        if problem_set != None:
            copy = problem_set.copy()
            i = 0
            while i < copy.get_length():
                self.add_problem(copy.get_problem(i))
                i = i + 1

    def set_points_per_problem(self,ppp):
        self.points_per_problem = ppp

    def get_points_per_problem(self):
        return self.points_per_problem

    def get_percent_per_question(self):
        return (100 * self.points_per_problem) / self.get_length()

def main():
    ps = ProblemSet()
    ps.load("checkme")
    exam = Exam("shit",1,ps)

if __name__ == "__main__" : main()
