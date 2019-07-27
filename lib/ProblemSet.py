#!/usr/bin/env python

#TODO
#Make this class more abstract
#Allow for any type of Problem to be saved/loaded
#Requires addition of save/load methods to Problem Objects

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

    def remove_problem(self, problem):
        for p in self.problems:
            if p is problem:
                self.problems.remove(p)
    def pop_problem(self):
        self.problems.pop()

    def get_problem(self,index):
        try:
            return self.problems[index]
        except IndexError:
            print("Specify a valid index: {} - {}".format(0,len(self.problems)))

    def get_length(self):
        return len(self.problems)
    
    def as_string(self):
        ret = self.name + "\n"
        for p in self.problems:
            ret = "{}{}".format(ret,p.as_string())
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

        lines = [s[:-1] for s in lines] 
        self.name = lines[0]
        i = 1
        self.problems = []
        
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

def test():
    a = Problem("1.) 10*10",100)
    b = Problem("2.) 10+10",20)
    c = Problem("3.) 10-10",0)
    d = Problem("4.) 10/10",1)
    e = Problem("5.) 10%10",0)
    f = MathProblem("6.) 100/10","10","Divide","Divide")
    g = MathProblem("7.) 100/10","10","Divide","Divide")
    h = MathProblem("8.) 100/10","10","Divide","Divide")
    i = Problem("9.) 10%10",0)
    j = MathProblem("10.) 100/10","10","Divide","Divide")
    k = Problem("11.) 10%10",0)

    pset = ProblemSet("Arithmetic Problem Set",a,b,c,d,e,f,g,h,i)
    pset.add_problem(j)
    pset.add_problem(k)
    assert (pset.get_problem(0) is a) , "get_problem(0)"
    assert (pset.get_name() == "Arithmetic Problem Set"), "naming"
    pset.save("checkme")

    load_set = ProblemSet(None)
    load_set.load("checkme")
    print(load_set.as_string()) 


if __name__ == "__main__": test()
