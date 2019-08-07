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
            if problem == self.problems[i]:
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

    #replaces the problem @ index with problem
    def replace_problem(self,index,problem):
        if self.check_index(index):
            self.problems[index] = problem
    
    #inserts problem before index 
    def insert_problem(self,index,problem):
        if not(self.check_index(index)):
            return

        temp = []
        for i in range(self.get_length()):
            if i == index:
                temp.append(problem)
            temp.append(self.problems[i])
        self.problems = temp.copy()

    def swap_problem(self,ind1,ind2):
        if not(self.check_index(ind1)and self.check_index(ind2))and(ind1 != ind2):
            return -1
        temp = self.problems[ind1]
        self.problems[ind1] = self.problems[ind2]
        self.problems[ind2] = temp

    def move_problem(self,org,dst):
        if not(self.check_index(org) and self.check_index(dst)) and (org != dst):
            return

        temp = []
        for i in range(self.get_length()):
            if i == dst:
                temp.append(self.problems[org])
            if i != org:
                temp.append(self.problems[i])

        self.problems = temp.copy()

    def pop_problem(self):
        self.problems.pop()

    def get_problem(self,index):
        if self.check_index(index):
            return self.problems[index]

    def get_length(self):
        return len(self.problems)
    
    def as_string(self):
        ret = self.name + "\n"
        for p in self.problems:
            ret = "{}{}".format(ret,p.as_string())
        return ret

    def as_numbered_string(self):
        ret = self.name + "\n"
        i = 0
        for p in self.problems:
            i = i + 1
            ret = "{}{}\n{}\n".format(ret,i,p.as_string())
        return ret

    def save(self,filename):
        try:
            with open(filename,'w') as f:
                f.write(self.as_string())           
        except FileNotFoundError:
            print("\"{}\" does not exist".format(filename))

    def load(self,filename):
        lines = []
        try:
            with open(filename,'r') as f:
                lines = f.readlines()
        except FileNotFoundError: 
            print("\"{}\" does not exist".format(filename))

        lines = [s[:-1] for s in lines] #remove newlines
        self.load_lines(lines)

    def load_lines(self,lines):
        self.name = lines[0]
        self.problems = []
        i = 1
        while i < len(lines):
            check = (re.findall("^Type:\"(.*)\"", lines[i]))[0]
            if check == "Problem":
                add = Problem()
            elif check == "MathProblem":
                add = MathProblem()
            else:
                print("error")
                return -1 
            i = add.load(lines,i)
            self.problems.append(add)

    #return a copy of the ProblemSet Obj
    def copy(self):
        cps = ProblemSet(self.name)

        if self.problems != None :
            for i in range(self.get_length()):
                cps.add_problem((self.problems[i]).copy())

        return cps

    def consolidate(self, ps, *args):
        for i in range(ps.get_length()):
            self.problems.append(ps.get_problem(i))
        for s in args:
            for i in range(s.get_length()):
                self.problems.append(s.get_problem(i))

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

    def check_index(self,i):
        if i < 0 or i > self.get_length():
            print("Specify a valid index: {} - {}".format(0,len(self.problems)))
            return False
        else:
            return True


#end of class

def test():
    pset = ProblemSet("Problem_Set")
    pset.test_fill_quotes()
    pset.test_fill_math(10)
    pset.test_fill(10)

    swap = ProblemSet("swap_test")
    swap.test_fill(10)
    first = swap.get_problem(0)
    last  = swap.get_problem(9)
    swap.swap_problem(0,9)
    assert((swap.get_problem(0)).as_string() == last.as_string()),"swap"
    assert((swap.get_problem(9)).as_string() == first.as_string()),"swap"
    swap.move_problem(9,0)
    assert((swap.get_problem(0)).as_string() == first.as_string()),"move"

    a = Problem("10*10",100)
    b = Problem("10+10",20)

    pset.add_problem(a)
    pset.add_problem(b)
    pset.remove_problem(b)

    pset.replace_problem(0,a)
    assert((pset.get_problem(0)).as_string() == a.as_string()) , "replace_problem(0,a)"


    pset.insert_problem(5,a)
    assert((pset.get_problem(5)).as_string() == a.as_string()) , "replace_problem(0,a)"

    assert (pset.find_problem(b) == -1),"remove_problem(k)"
    assert (pset.get_problem(pset.get_length()-1) is a) , "get_problem(0)"
    assert (pset.get_name() == "Problem_Set"), "naming"
    pset.save("checkme")

    load_set = ProblemSet()
    load_set.load("checkme")
    assert(pset.as_string() == load_set.as_string()),"loading/saving error"

    copy_set = load_set.copy()
    assert ( (copy_set is load_set) == False ), "copy()"
    assert ( copy_set.as_string() == load_set.as_string()), "copy()"

    p1 = ProblemSet()
    p2 = ProblemSet()
    p3 = ProblemSet()

    p1.test_fill_quotes()
    p2.test_fill_math(7)
    p3.test_fill(7)
    test_string = (p1.as_string()).rstrip() + (p2.as_string()).rstrip() + p3.as_string()
    p1.consolidate(p2,p3)
    assert(p1.as_string() == test_string), "consolidate"

if __name__ == "__main__": test()
