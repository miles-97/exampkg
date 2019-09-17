#!/usr/bin/env python3

import unittest
from lib.Problem    import Problem

class ProblemTest(unittest.TestCase):

    def setUp(self):
        self.q = "Question"
        self.a = "Answer"
        self.p  = Problem(self.q,self.a)

    def test_get_question(self):
        self.assertEqual(self.p.get_question(),self.q)

    def test_get_answer(self):
        self.assertEqual(self.p.get_answer(),self.a)

    def test_set_question(self):
        self.p.set_question("New Question")
        self.assertEqual(self.p.get_question(),"New Question")

    def test_set_answer(self):
        self.p.set_answer("New Answer")
        self.assertEqual(self.p.get_answer(),"New Answer")

    def test_check_answer(self):
        self.assertTrue(self.p.check_answer(self.a))
        self.assertFalse(self.p.check_answer("not the answer"))

    def test_as_string(self):
        test_string = "Problem|Question|Answer|"
        self.assertEqual(self.p.as_string(),test_string)

    def test_copy(self):
        copy = self.p.copy()
        self.assertFalse(self.p is copy)
        self.assertEqual(self.p.as_string(),copy.as_string())

if __name__ == "__main__" : unittest.main()
