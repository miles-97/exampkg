#!/usr/bin/env python3

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet
import random

class Exam(ProblemSet):
    points = []

    def __init__(self,name="",points=None,problem_set=None):
        super(Exam,self).__init__(name)
        if problem_set != None and points != None : 
            self.points = points.copy()
            copy = problem_set.copy()
            i = 0
            while i < copy.get_length():
                super(Exam,self).add_problem(copy.get_problem(i))
                i = i + 1

    def add_problem(self,problem,points):
        super(Exam,self).add_problem(problem.copy())
        self.points.append(points)

    def remove_problem(self, problem):
        index = self.find_problem(problem)
        if super(Exam,self).remove_problem(problem) == 0:
            self.points.pop(index)
            return 0
        else:
            return -1

    def pop_problem(self):
        self.problems.pop()
        self.points.pop()

    def save(self,filename):
        super(Exam,self).save(filename) #write problemset

        try:
            with open(filename,'r+') as f:
                content = f.read() #copy problemset
                f.seek(0,0)
                for p in self.points:
                    f.write("{} ".format(p)) #write points to SOF
                f.write('\n' + content) #rewrite problemset
        except FileNotFoundError:
            print("\"{}\" does not exist",format(filename))

    def load(self,filename):
        lines = []

        try:
            with open(filename,'r') as f:
                lines = f.readlines() #copy problemset
        except FileNotFoundError:
            print("\"{}\" does not exist",format(filename))

        lines = [s[:-1] for s in lines] #strip \n
        str_points = lines[0].split(" ") #get points as string
        points = []
        for s in str_points: #reassigning to org arr fails bc last element is always ''
            if s.isdigit():
                points.append(int(s))
        self.points = points
        del lines[0] #first line is points so delete them before passing lines to super
        super(Exam,self).load_lines(lines)

    def get_points_of_problem(self,index):
        try:
            return self.points[index]
        except IndexError:
            print("Out of range")

    def get_percent_of_problem(self,index):
        try:
            return self.points[index] / sum(self.points)
        except IndexError:
            print("Out of range")

    def get_percent_of_problem_rounded(self,index):
        return round(get_percent_of_problem(index),2)

    def get_points(self):
        return self.points

    def get_total_points(self):
        return sum(self.points)

#n = number of problems
def fill_problem_set(n):
    ps = ProblemSet()
    questions = [ "Will you descend into the belly of the whale?",
            "Will you integrate your shadow?",
            "Will you clean up your room?",
            "Will you seek out a heavy load?",
            "Will you leave Neverland?",
            "Will you stand up straight with your shoulders back?",
            "Will you say what you think?"]
    for i in range(n):
        if i > len(questions)-1:
            prob = Problem("Q"+str(i) , "A"+str(i))
        else:
            prob = Problem(questions[i],"Yes")
        ps.add_problem(prob)

    return ps

def fill_points_list(n):
    l = []
    for i in range(n):
        l.append(random.randint(1,5))
    return l

def test():
    ps = ProblemSet("Problem_Set")
    ps.test_fill(10)
    points = fill_points_list(10)
    
    exam = Exam("Exam_Test",points,ps)

    prob = Problem("Q_Test","Q_Ans")
    exam.add_problem(Problem("Q_Test","Q_Ans"),5)
    points.append(5)

    assert (exam.get_total_points() == sum(points)), "get_total_points()"
    assert (exam.get_points() == points), "get_points()"

    exam.save("exam_test")
    load_exam = Exam()
    load_exam.load("exam_test")
   
    assert(load_exam.as_string() == exam.as_string()),"load/save"
    assert(load_exam.get_points() == exam.get_points()),"load/save"
    assert(load_exam.get_percent_of_problem(0) == exam.get_percent_of_problem(0)),"get % prob"

    load_exam.remove_problem(prob)
    assert(load_exam.find_problem(prob) == -1), "remove_problem"

#end of test()

if __name__ == "__main__" : test()
