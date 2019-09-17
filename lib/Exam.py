#!/usr/bin/env python3

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet
import random

class Exam(ProblemSet):
    points = []

    def __init__(self,name="",points=None,problem_set=None):
        self.points = []
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
            return 0
        else:
            return -1

    def replace_problem(self,index,problem,point_val):
        if self.check_index(index):
            self.problems[index] = problem.copy()
            self.points[index] = point_val
            return 0
        else:
            return -1

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
        return 0

    def move_problem(self,org,dst):
        super(Exam,self).move_problem(org,dst)

        temp = []
        for i in range(self.get_length()):
            if i == dst:
                temp.append(self.points[org])
            if i != org:
                temp.append(self.points[i])
        self.points = temp.copy()
        return 0

    def pop_problem(self):
        self.problems.pop()
        self.points.pop()

    def as_string(self):
        lines = (super(Exam,self).as_string()).split("\n")
        point_str = ' '.join([str(p) for p in self.points]) #get points as string
        lines.insert(1, point_str)
        return '\n'.join(lines)
 
    # cheeky solution to get around python's lack of method overloading
    # Exam init can only take in problemsets, super.copy() serves as an
    # Exam -> ProblemSet conversion function. Letting a problemset be 
    # passed to init. A bit wasteful since self is copied twice
    def copy(self):
        return Exam(self.name,self.points,super(Exam,self).copy())

    def save(self,filename):
        with open(filename,'w') as f:
            f.write(self.as_string())

    def load(self,filename):
        with open(filename,'r') as f:
            lines = f.readlines()

        self.name = lines[0].rstrip()
        temp_points = [ int(num) for num in lines[1].rstrip().split() ]
        for i in range(2,len(lines)):
            values = lines[i].split("|") #get | seperated values
            if values[0] == "Problem":
                p = Problem(values[1],values[2])
            elif values[0] == "MathProblem":
                p = MathProblem(values[1],values[2],values[3],values[4])
            self.add_problem(p,temp_points[i-2])

    def consolidate(self,exam,*args):
        super(Exam,self).consolidate(exam,*args)

        self.points = exam.get_points().copy()
        for e in args:
            self.points += e.get_points().copy()

    def get_points_of_problem(self,index):
        if self.check_index(index):
            return self.points[index]
        else:
            return -1

    def get_percent_of_problem(self,index):
        if self.check_index(index):
            return self.points[index] / sum(self.points)
        else:
            return -1

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
            self.add_problem(Problem(q,"Yes"),random.randint(1,7))

    def as_text_file(self,filename):
        with open(filename,'w') as f:
            f.write("\t\t{}\n".format(self.get_name()))
            for i in range(self.get_length()):
                f.write("{}.) {} ({})\n\n\n".format(i+1,self.get_problem(i).get_question(),self.points[i]))


if __name__ == "__main__" : 
    print("Testing moved to test/Test_Exam.py")
