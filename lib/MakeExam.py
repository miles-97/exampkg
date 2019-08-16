#!/usr/bin/env python3

from lib.Problem        import Problem
from lib.MathProblem    import MathProblem
from lib.ProblemSet     import ProblemSet
from lib.Exam           import Exam

#checks user input against yes/no for a given string
#true on yes, false on no
def get_user_continue(string):
    while True:
        u_choice = input("{} {}".format(string,(" (y / n): ")))
        if u_choice == "n":
            return False
        elif u_choice == "y":
            return True
        else: 
            print("Input not recognized. Enter \'y\' or \'n\'")

#gets input from user with verification
def get_user_input(string):
    u_input = ""
    loop = True
    while loop:
        u_input = input("Enter {}: ".format(string))
        if u_input == "":
            print("Can't intialize a null ", string ," . Try again.")
            continue
        if get_user_continue("Is this,\"{}\", right?".format(u_input)):
            break
        else:
            continue 
    return u_input

#prompts user for components of a problem
def create_problem():
    u_question = get_user_input("question")
    u_answer = get_user_input("answer")
    return Problem(u_question, u_answer)

def create_problem_set():
    if get_user_continue("Would you like to create a problem set?")==False:
        return
    #else     
    ps = ProblemSet(get_user_input("name"))
    while True:
        print( "1.) Add Problems")
        print( "2.) View Problem Set")
        print( "3.) Save Problem Set")
        print("99.) Exit")
        u_choice = input("Enter your choice: ")
        if   u_choice == "1":
            while get_user_continue("Would you like to add a problem?"):
                ps.add_problem(create_problem())
        elif u_choice == "2":
            print(ps.as_string())
        elif u_choice == "3":
            ps.save(get_user_input("filename"))
        elif u_choice == "99":
            if get_user_continue("Are you sure you'd like to continue? Any unsaved date will be lost."):
                return
            else:
                continue

def create_exam():
    if get_user_continue("Would you like to create an exam?")==False:
        return
    #else     
    exam = Exam(get_user_input("name"))
    while True:
        print( "1.) Add Problems")
        print( "2.) View Exam")
        print( "3.) Save Exam")
        print("99.) Exit")
        u_choice = input("Enter your choice: ")
        if   u_choice == "1":
            while get_user_continue("Would you like to add a problem?"):
                problem = create_problem()
                points = int(get_user_input("Point Value"))
                exam.add_problem(problem,points)
        elif u_choice == "2":
            print(exam.as_string())
        elif u_choice == "3":
            exam.save(get_user_input("filename"))
        elif u_choice == "99":
            if get_user_continue("Are you sure you'd like to continue? Any unsaved date will be lost."):
                return
            else:
                continue

def modify_problem_set():
    filename = get_user_input("Filename where Problem Set is stored: ")
    ps = ProblemSet()
    ps.load(filename)

    while True:
        print(" 1.) View Problem Set")
        print(" 2.) Delete Problem")
        print(" 3.) Move Problem")
        print(" 4.) Add New Problem")
        print(" 5.) Insert New Problem")
        print(" 6.) Consolidate with Existing Problem Set")
        print(" 7.) Delete Problem Set")
        print("98.) Help")
        print("99.) Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(ps.as_numbered_string())
        elif choice == '2':
            index = -1
            while ps.remove_problem(index) == -1:
                index = get_user_input("Problem Number: ")
    
        elif choice == '3':
            print("I have no purpose")
        elif choice == '4':
            print("I have no purpose")
        elif choice == '5':
            print("I have no purpose")
        elif choice == '6':
            print("I have no purpose")
        elif choice == '7':
            print("I have no purpose")
        elif choice == '98':
            print("I can't help ya bucko.")
        elif choice == '99':
            print("Exiting Modify Problem Set Menu")
            return
        else:
            print("Unrecognized Input")

def modify_exam():
    print("I do nothing right now")

def view_problem_set():
    print("I do nothing right now")

def view_exam():
    print("I do nothing right now")

def help_me():
    print("I can't help you, yet")

def _exit():
    print("Bye. Bye.")
    exit()

def main():
    while True:
        print("\nMain Menu\n")
        print("\t01.) Create new problem set")
        print("\t02.) Create new exam")
        print("\t03.) Modify problem set")
        print("\t04.) Modify exam")
        print("\t05.) View problem set")
        print("\t06.) View exam")
        print("\t98.) Help")
        print("\t99.) Exit")
        user_input = input("\tEnter your choice: ")
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
            _exit()
        else: 
            print("Input not recognized")

def test():
    main()


if __name__ == "__main__" : test()
