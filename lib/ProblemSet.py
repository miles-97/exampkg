#!/usr/bin/env python3

import re
from lib.Problem import Problem
from lib.MathProblem import MathProblem

class ProblemSet:
    __problems = []
    __name = "" #name of ProblemSet

    def __init__(self,name="",*problems):
        self.problems = []
        self.name = name
        if problems != [None]:
            for p in problems:
                self.problems.append(p)

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def add_problem(self, problem):
        self.problems.append(problem)

    #returns index of a problem or -1 if it is not in this problemset
    def find_problem(self, problem):
        for i in range(len(self.problems)):
            if problem.as_string() == self.problems[i].as_string():
                return i
        return -1
            
    #returns 0 if remove was successful
    #returns -1 if problem is not in problem set
    def remove_problem(self, problem):
        index = self.find_problem(problem)
        if index != -1:
            self.problems.remove(problem)
            return 0
        else:
            return -1

    def remove_index(self, index):
        if self.check_index(index):
            self.problems.pop(index)
            return 0
        else:
            return -1

    #replaces the problem @ index with problem
    def replace_problem(self,index,problem):
        if self.check_index(index):
            self.problems[index] = problem
        return -1
    
    #inserts problem before index 
    def insert_problem(self,index,problem):
        if not(self.check_index(index)):
            return -1

        temp = []
        for i in range(self.get_length()):
            if i == index:
                temp.append(problem)
            temp.append(self.problems[i])
        self.problems = temp.copy()
        return 0

    def swap_problem(self,ind1,ind2):
        if not(self.check_index(ind1)) or not(self.check_index(ind2)) or (ind1 == ind2):
            return -1
        temp = self.problems[ind1]
        self.problems[ind1] = self.problems[ind2]
        self.problems[ind2] = temp
        return 0

    def move_problem(self,org,dst):
        if not(self.check_index(org)) or not(self.check_index(dst)) or (org == dst):
            return -1

        temp = []
        if org < dst:
            for i in range(self.get_length()):
                if i != org:
                    temp.append(self.problems[i])
                if i == dst:
                    temp.append(self.problems[org])
        else:
            for i in range(self.get_length()):
                if i == dst:
                    temp.append(self.problems[org])
                if i != org:
                    temp.append(self.problems[i])

        self.problems = temp.copy()
        return 0

    def pop_problem(self):
        self.problems.pop()

    def get_problem(self,index):
        if self.check_index(index):
            return self.problems[index]

    def get_length(self):
        return len(self.problems)
    
    #return a copy of the ProblemSet Obj
    def copy(self):
        return ProblemSet(self.name,*[p.copy() for p in self.problems])

    def consolidate(self, ps, *args):
        for i in range(ps.get_length()):
            self.problems.append(ps.get_problem(i))
        for s in args:
            for i in range(s.get_length()):
                self.problems.append(s.get_problem(i))

    def check_index(self,i):
        if i < 0 or i >= self.get_length():
            return False
        else:
            return True

    def as_string(self):
        return self.name+ '\n' + ''.join([(p.as_string() + "\n") for p in self.problems])

    def save(self,filename):
        with open(filename,'w') as f:
            f.write(self.as_string())

    def load(self,filename):
        with open(filename,'r') as f:
            lines = f.readlines()

        self.name = lines[0].rstrip()
        for i in range(1,len(lines)):
            values = lines[i].split("|") #get | seperated values
            p = ""
            if values[0] == "Problem":
                p = Problem(values[1],values[2])
            elif values[0] == "MathProblem":
                p = MathProblem(values[1],values[2],values[3],values[4])
            self.add_problem(p)

    def as_text_file(self,filename):
        with open(filename,'w') as f:
            for i in range(len(self.problems)):
                f.write("{}.) {}\n\n".format(i+1,self.problems[i].get_question()))


    def test_fill_quotes(self):
        questions = [ "Will you descend into the belly of the whale?",
            "Will you integrate your shadow?",
            "Will you clean up your room?",
            "Will you seek out a heavy load?",
            "Will you leave Neverland?",
            "Will you stand up straight with your shoulders back?",
            "Will you say what you think?"]

        for q in questions:
            self.add_problem(Problem(q,"Yes"))

    def test_fill(self,n):
        for i in range(n):
            ind = str(self.get_length()+1)
            self.add_problem(Problem("Q"+str(ind) , "A"+str(ind)))

    def test_fill_math(self,n):
        for i in range(n):
            ind = str(self.get_length()+1)
            self.add_problem(MathProblem("Q"+ind , "A"+ind, "S"+ind, "H"+ind))

#end of class

if __name__ == "__main__": 
    print("testing moved to test/Test_ProblemSet.py")
