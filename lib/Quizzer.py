#!/usr/bin/env python3

import sys
import os.path

from lib.Problem        import Problem
from lib.ProblemSet     import ProblemSet
from lib.MathProblem    import MathProblem
from lib.Exam           import Exam

def administer_problem_set(ps):
    score = 0 
    for i in range(ps.get_length()):
        if prompt_question(ps.get_problem(i)):
            score += 1
        else:
            print("Right Answer:{}".format(ps.get_problem(i).get_answer()))
    print("({}/{})".format(score,ps.get_length()))

def administer_exam(ex):
    score = 0
    for i in range(ex.get_length()):
        if prompt_question(ex.get_problem(i)):
            score += ex.get_points_of_problem(i)
        else:
            print("Right Answer:{}".format(ex.get_problem(i).get_answer()))
    print("({}/{})".format(score,ex.get_total_points()))

def prompt_question(p):
    return p.check_answer(input("{}\n".format(p.get_question())))


def print_help():
    print("Usage:")
    print("\t\'python3 Quizzer.py -e file_name\' Administers an Exam")
    print("\t\'python3 Quizzer.py -p file_name\' Administers a ProblemSet")
    exit()

def main():
    if len(sys.argv) == 3:
        option   = sys.argv[1]
        filename = sys.argv[2]
        if option == "-e" and os.path.isfile(filename):
            exam = Exam()
            exam.load(filename)
            administer_exam(exam)
        elif option == "-p" and os.path.isfile(filename):
            ps = ProblemSet()
            ps.load(filename)
            administer_problem_set(ps)
        else:
            print_help()
    else:
        print_help()

if __name__ == "__main__" : main()
