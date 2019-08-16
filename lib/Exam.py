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
            temp = problem_set.copy()
            for i in range(temp.get_length()):
                self.problems.append(temp.get_problem(i))

    def add_problem(self,problem,point_val):
        super(Exam,self).add_problem(problem.copy())
        self.points.append(point_val)

    def remove_problem(self, problem):
        index = self.find_problem(problem)
        if super(Exam,self).remove_problem(problem) == 0:
            self.points.pop(index)
        else:
            return -1

    def replace_problem(self,index,problem,point_val):
        if self.check_index(index):
            self.problems[index] = problem.copy()
            self.points[index] = point_val

    def insert_problem(self,index,problem,point_val):
        if not(self.check_index(index)):
            return -1
        temp = []
        for i in range(len(self.points)):
            if i == index:
                temp.append(point_val)
            temp.append(self.points[i])
        self.points = temp.copy()
        super(Exam,self).insert_problem(index,problem)

    def swap_problem(self,ind1,ind2):
        if super(Exam,self).swap_problem(ind1,ind2) == -1:
            return -1
        temp = self.points[ind1]
        self.points[ind1] = self.points[ind2]
        self.points[ind2] = temp

    def move_problem(self,org,dst):
        super(Exam,self).move_problem(org,dst)

        temp = []
        for i in range(self.get_length()):
            if i == dst:
                temp.append(self.points[org])
            if i != org:
                temp.append(self.points[i])
        self.points = temp.copy()

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

    def consolidate(self,exam,*args):
        super(Exam,self).consolidate(exam,*args)

        for i in range(exam.get_length()):
            self.points.append(exam.get_points_of_problem(i))
        for e in args:
            for i in range(e.get_length()):
                self.points.append(e.get_points_of_problem(i))

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
    
    def test_fill_points(self,n):
        for i in range(n):
            self.points.append(random.randint(1,5))

    def test_fill_quotes(self):
        questions = [ "Will you descend into the belly of the whale?",
            "Will you integrate your shadow?",
            "Will you clean up your room?",
            "Will you seek out a heavy load?",
            "Will you leave Neverland?",
            "Will you stand up straight with your shoulders back?",
            "Will you say what you think?"]

        for q in questions:
            self.add_problem(Problem(q,"Yes"),1)


    def as_text_file(self,filename):
        with open(filename,'w') as f:
            f.write("\t\t{}\n".format(self.get_name()))
            for i in range(self.get_length()):
                f.write("{}.) {} ({})\n\n\n".format(i+1,self.get_problem(i).get_question(),self.points[i]))

def fill_points(n):
    l = []
    for i in range(n):
        l.append(random.randint(1,5))
    return l

def test():
    ps = ProblemSet("Problem_Set")
    ps.test_fill(10)
    points = fill_points(10)

    exam = Exam("Exam_Test",points,ps)

    prob = Problem("Q_Test","Q_Ans")
    exam.add_problem(prob,5)
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
    
    a = load_exam.get_problem(0)
    ap = load_exam.get_points_of_problem(0)
    b = load_exam.get_problem(9)
    bp = load_exam.get_points_of_problem(9)

    load_exam.swap_problem(0,9)
    assert(load_exam.get_problem(0).as_string() == b.as_string()),"swap"
    assert(load_exam.get_points_of_problem(0) == bp),"swap"
    assert(load_exam.get_problem(9).as_string() == a.as_string()),"swap"
    assert(load_exam.get_points_of_problem(9) == ap),"swap"

    c = Problem("Ins Prob","Ins Ans")
    load_exam.insert_problem(5,c,3)
    assert(load_exam.get_problem(5).as_string() == c.as_string()),"ins"
    assert(load_exam.get_points_of_problem(5) == 3),"in"

    d = load_exam.get_problem(1)
    dp = load_exam.get_points_of_problem(1)
    load_exam.move_problem(1,10)
    assert(load_exam.get_problem(9).as_string() == d.as_string()),"move"
    assert(load_exam.get_points_of_problem(9) == dp),"move"

    ps1 = ProblemSet()
    ps2 = ProblemSet()
    ps3 = ProblemSet()
    ps1.test_fill(7)
    ps2.test_fill_quotes()
    ps3.test_fill_math(7)
    e1 = Exam("consolidate1",fill_points(7),ps1)
    e2 = Exam("consolidate1",fill_points(7),ps2)
    e3 = Exam("consolidate1",fill_points(7),ps3)
    test_string = (e1.as_string()).rstrip() + (e2.as_string()).rstrip() + e3.as_string()
    e1.consolidate(e2,e3)
    assert(e1.get_problem(7).as_string() == e2.get_problem(0).as_string()),"consolidate"
    assert(e1.get_problem(14).as_string() == e3.get_problem(0).as_string()),"consolidate"

    text_exam = Exam("Meaning Test")
    text_exam.test_fill_quotes()
    text_exam.as_text_file("Meaning_Test.txt")

#end of test()

if __name__ == "__main__" : test()
