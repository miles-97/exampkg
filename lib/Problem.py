#!/usr/bin/env python3

import re

class Problem:
    __question = ""
    __answer = ""
    __type = ""

    def __init__(self,question="",answer=""): 
        self.question = question
        self.answer = answer
        self.type = "Problem"

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def set_question(self,question):
        self.question = question

    def set_answer(self,answer):
        self.answer = answer

    def check_answer(self,a):
        return (self.answer == a)

    def as_string(self):
        return "Type:\"{}\"\nQuestion:\"{}\"\nAnswer:\"{}\"\n".format(self.type,self.question,self.answer)
    
    def load(self,lines,index):
        x = re.findall("^Type:\"(.*)\"", lines[index])
        y = (re.findall("^Question:\"(.*)\"", lines[index+1]))[0]
        z = (re.findall("^Answer:\"(.*)\"", lines[index+2]))[0]
        self.question = y
        self.answer = z
        return index + 3

    def copy(self):
        return Problem(self.question,self.answer)

#end of Problem class

def test_problem():
    q1 = "meaning of life?"
    a1 = "42"
    q2 = "new question"
    a2 = "new answer"
    a = Problem(q1,a1)
    assert (a.get_question() == q1) , "get_question"
    assert (a.get_answer() == a1) , "get_answer"
    assert (a.check_answer(a1) == True) , "check_answer"
    a.set_question(q2)
    assert (a.get_question() == q2) , "get_question"
    a.set_answer(a2)
    assert (a.get_answer() == a2) , "get_answer"
    assert (a.check_answer(a2) == True),"check_answer"
    #print(a.as_string())

def test_load():
    a = Problem()
    b = Problem()
    lines = ["Type:\"Problem\"","Question:\"Q1\"","Answer:\"A1\"","Type:\"Problem\"","Question:\"Q2\"","Answer:\"A2\""]

    i = a.load(lines,0)
    b.load(lines,i) 

    assert (a.get_question() == "Q1"),"test-load, a.get_question"
    assert (b.get_question() == "Q2"),"test-load, b.get_question"
    assert (a.get_answer() == "A1"),"test-load, a.get_answer"
    assert (b.get_answer() == "A2"),"test-load, b.get_answer"
    #print(a.as_string())
    #print(b.as_string())

def test_copy():
    a = Problem("What letter comes after B?","C")
    b = a.copy()
    assert ( (a is b) == False ), "copy()"
    assert ( a.as_string() == b.as_string()), "copy()"

def test():
    test_problem()
    test_load()
    test_copy()

if __name__ == "__main__": test()
