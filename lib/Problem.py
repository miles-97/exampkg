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
        return "Problem|{}|{}|".format(self.question,self.answer)
    
    def copy(self):
        return Problem(self.question,self.answer)


if __name__ == "__main__": 
    print("Testing was moved to Test_Problem.py")
