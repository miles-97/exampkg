#!/usr/bin/env python3

from lib.Problem import Problem
from lib.MathProblem import MathProblem
from lib.ProblemSet import ProblemSet

def create_problem_set():
    print("I do nothing right now")

def create_exam():
    print("I do nothing right now")

def modify_problem_set():
    print("I do nothing right now")

def modify_exam():
    print("I do nothing right now")

def view_problem_set():
    print("I do nothing right now")

def view_exam():
    print("I do nothing right now")

def help_me():
    print("I can't help you, yet")

def main():
    while True:
        print("Main Menu")
        print("\t01.) Create new problem set")
        print("\t02.) Create new exam")
        print("\t03.) Modify problem set")
        print("\t04.) Modify exam")
        print("\t05.) View problem set")
        print("\t06.) View exam")
        print("\t98.) Help")
        print("\t99.) Exit")
        user_input = input("\tEnter your choice:")
        if user_input == "1":
            create_problem_set()
        elif user_input == '2':
            create_exam()
        elif user_input == '3':
            modify_problem_set()
        elif user_input == '4':
            modify_exam()
        elif user_input == '5':
            view_problem_set()
        elif user_input == '6':
            view_exam()
        elif user_input == '98':
            help_me()
        elif user_input == '99':
            exit()
        else: 
            print("Input not recognized")



if __name__ == "__main__" : main()
