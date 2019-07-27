#!/usr/bin/env python

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet

def test_problem():
    q1 = "meaning of life?"
    a1 = "42"
    q2 = "Will you descend into the belly of the whale?"
    a2 = "Yes"
    a = Problem(q1,a1)
    assert (a.get_question() == q1) , "get_question"
    assert (a.get_answer() == a1) , "get_answer"
    assert (a.check_answer(a1) == True) , "check_answer"
    a.set_question(q2)
    assert (a.get_question() == q2) , "get_question"
    a.set_answer(a2)
    assert (a.get_answer() == a2) , "get_answer"
    assert (a.check_answer(a2) == True),"check_answer"
    print(a.as_string())
    print("\nEnd of Problem Test\n")

def test_math_problem():
    q1 = "What's 10 * 10?"
    a1 = 100
    s1 = "multiplication"
    h1 = "multiplication"
    q2 = "What's 20 / 2"
    s2 = "division"
    h2 = "division"
    a2 = 10
    b = MathProblem(q1,a1,s1,h1)
    assert (b.get_question() == q1) , "get_question"
    assert (b.get_answer() == a1) , "get_answer"
    assert (b.get_hint() == h1), "get_hint"
    assert (b.get_solution() == s1), "get_solution"
    assert (b.check_answer(a1) == True) , "check_answer"
    print(b.as_string())

    b.set_question(q2)
    b.set_answer(a2)
    b.set_hint(h2)
    b.set_solution(s2)
    assert (b.get_question() == q2) , "get_question"
    assert (b.get_answer() == a2) , "get_answer"
    assert (b.get_hint() == h2) , "get_hint"
    assert (b.get_solution() == s2) , "get_solution"
    assert (b.check_answer(a2) == True),"check_answer"

    print(b.as_string())
    print("\nEnd of Math Problem Test\n")

def test_problem_set():
    a = Problem("10*10",100)
    b = Problem("10+10",20)
    c = Problem("10-10",0)
    d = Problem("10/10",1)
    e = Problem("10%10",0)

    pset = ProblemSet("Arithmetic Problem Set",a,b,c,d)
    pset.add_problem(e)
    assert (pset.get_problem(0) is a) , "get_problem(0)"
    assert (pset.get_problem(1) is b) , "get_problem(1)"
    assert (pset.get_problem(2) is c) , "get_problem(2)"
    assert (pset.get_problem(3) is d) , "get_problem(3)"
    assert (pset.get_problem(4) is e) , "get_problem(4)"
    assert (pset.get_name() == "Arithmetic Problem Set"), "naming"
    pset.save("checkme")

    load_set = ProblemSet(None)
    load_set.load("checkme")
    print(load_set.as_string())
    print("\nEnd of Problem Set Test\n")

def test():
    test_problem()
    test_math_problem()
    test_problem_set()

if __name__ == "__main__": test()
