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
        return "{}Solution:\"{}\"\nHint:\"{}\"\n".format(Problem.as_string(self),self.solution,self.hint)

    def load(self,lines,index):
        a = (re.findall("^Question:\"(.*)\"",lines[index+1]))[0]
        b = (re.findall("^Answer:\"(.*)\"",lines[index+2]))[0]
        c = (re.findall("^Solution:\"(.*)\"",lines[index+3]))[0]
        d = (re.findall("^Hint:\"(.*)\"",lines[index+4]))[0]
        self.question = a
        self.answer = b
        self.solution = c
        self.hint = d
        return index + 5

    def copy(self):
        return MathProblem(self.question,self.answer,self.solution,self.hint)

def test():
    q1 = "What's 10 * 10?"
    a1 = 100
    s1 = "multiplication"
    h1 = "multiplication"
    q2 = "What's 20 / 2"
    s2 = "division"
    h2 = "division"
    a2 = 10
    a = MathProblem(q1,a1,s1,h1)
    assert (a.get_question() == q1) , "get_question"
    assert (a.get_answer() == a1) , "get_answer"
    assert (a.get_hint() == h1), "get_hint"
    assert (a.get_solution() == s1), "get_solution"
    assert (a.check_answer(a1) == True) , "check_answer"
    #print(a.as_string())

    a.set_question(q2)
    a.set_answer(a2)
    a.set_hint(h2)
    a.set_solution(s2)
    assert (a.get_question() == q2) , "get_question"
    assert (a.get_answer() == a2) , "get_answer"
    assert (a.get_hint() == h2) , "get_hint"
    assert (a.get_solution() == s2) , "get_solution"
    assert (a.check_answer(a2) == True),"check_answer"
    #print(a.as_string())

    lines = ["Type:\"MathProblem\"","Question:\"Q1\"","Answer:\"A1\"","Solution:\"S1\"","Hint:\"H1\"","Type:\"MathProblem\"","Question:\"Q2\"","Answer:\"A2\"","Solution:\"S2\"","Hint:\"H2\""]

    loadtest1 = MathProblem()
    loadtest2 = MathProblem()

    index = loadtest1.load(lines,0)
    loadtest2.load(lines,index)

    print(loadtest1.as_string())
    print(loadtest2.as_string())



if __name__ == "__main__": test()
