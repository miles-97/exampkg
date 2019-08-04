#!/usr/bin/env python3

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet

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
        elif problem_set == None and points == None :
            this_line_does_nothing = 0
        else:
            print("You must init points and problem_set at the same time")

    def add_problem(self,problem,points):
        super(Exam,self).add_problem(problem.copy())
        self.points.append(points)

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
        for s in str_points:
            if s.isdigit():
                points.append(int(s))
        self.points = points
        del lines[0]
        super(Exam,self).load_lines(lines)

    def get_points_of_problem(self,index):
        try:
            return self.points[index]
        except IndexError:
            print("Out of range")

    def get_percent_of_problem(self,index):
        try:
            total = 0
            for x in self.points:
                total = total + x
            return self.points[index] / total
        except IndexError:
            print("Out of range")

    def get_percent_of_problem_rounded(self,index):
        return round(get_percent_of_problem(index),2)

    def get_points(self):
        return self.points

    def get_total_points(self):
        total = 0
        for i in self.points:
            total += i

        return total

def test():
    ps = ProblemSet()
    ps.load("checkme")
    
    test_list = [1,2,1,3,4,2,1,1,2,1,1]
    exam = Exam("Exam_Test",test_list,ps)

    prob = Problem("Will you leave NeverLand?","Yes")
    exam.add_problem(prob,5)
    test_list.append(5)

    assert (exam.get_total_points() == 24), "get_total_points()"
    assert (exam.get_points() == test_list), "get_points()"

    exam.save("exam_test")
    load_exam = Exam()
    load_exam.load("exam_test")

    assert(load_exam.as_string() == exam.as_string()),"load/save"
    assert(load_exam.get_points() == exam.get_points()),"load/save"

if __name__ == "__main__" : test()
