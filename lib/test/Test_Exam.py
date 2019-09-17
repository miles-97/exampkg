#!/usr/bin/env python3

import unittest
from lib.Problem        import Problem
from lib.ProblemSet     import ProblemSet
from lib.Exam           import Exam

class ExamTest(unittest.TestCase):

    def setUp(self):
        self.name = "Exam"
        self.exam = Exam(self.name)
        self.exam.test_fill_quotes()
        #self.exam.save("setup")
        self.problemA = Problem("Question A","Answer A")
        self.problemB = Problem("Question B","Answer B")
        self.problemC = Problem("Question C","Answer C")

    def tearDown(self):
        del self.exam
        del self.problemA
        del self.problemB
        del self.problemC

    def test_get_name(self):
        self.assertEqual(self.name, self.exam.get_name())

    def test_set_name(self):
        self.exam.set_name("MyExam")
        self.assertEqual("MyExam" , self.exam.get_name())

    def test_find_problem(self):
        self.assertEqual(self.exam.find_problem(self.problemA), -1)
        self.exam.add_problem(self.problemA,1)
        self.exam.add_problem(self.problemB,1)
        self.exam.add_problem(self.problemC,1)
        indA = self.exam.find_problem(self.problemA)
        indB = self.exam.find_problem(self.problemB)
        indC = self.exam.find_problem(self.problemC)
        self.assertEqual(self.exam.get_problem(indA).as_string(),self.problemA.as_string())
        self.assertEqual(self.exam.get_problem(indB).as_string(),self.problemB.as_string())
        self.assertEqual(self.exam.get_problem(indC).as_string(),self.problemC.as_string())

    def test_remove_problem(self):
        self.assertEqual(self.exam.remove_problem(self.problemA),-1)

        p = self.exam.get_problem(0)
        self.assertEqual(self.exam.remove_problem(p),0)
        self.assertEqual(self.exam.find_problem(p), -1)

    def test_replace_problem(self):
        p = self.exam.get_problem(0)
        self.assertTrue(self.exam.check_index(0))
        self.assertEqual(self.exam.replace_problem(0,self.problemA,1), 0)
        self.assertEqual(self.exam.find_problem(p), -1)
        self.assertEqual(self.exam.find_problem(self.problemA), 0)

    def test_insert_problem(self):
        p = self.exam.get_problem(5)
        self.exam.insert_problem(5,self.problemA,1)
        self.assertEqual(self.exam.get_problem(5),self.problemA)
        self.assertEqual(self.exam.get_problem(6),p)

    def test_swap_problem(self):
        self.assertEqual(self.exam.swap_problem(-1,1),-1)
        self.assertEqual(self.exam.swap_problem(0,0),-1)
        self.assertEqual(self.exam.swap_problem(1,-1),-1)

        p0 = self.exam.get_problem(0) #problem in position zero orginally
        p1 = self.exam.get_problem(1) #problem in position one  orginally
        self.assertEqual(self.exam.swap_problem(0,1),0)
        self.assertEqual(self.exam.get_problem(0),p1) #p1 should be in pos 0
        self.assertEqual(self.exam.get_problem(1),p0) #p0 should be in pos 1

    def test_move_problem(self):
        #dst > org
        ind_org = 0
        ind_dst = 5
        prob_org = self.exam.get_problem(ind_org)
        prob_dst = self.exam.get_problem(ind_dst)
        self.assertEqual(self.exam.move_problem(ind_org,ind_dst), 0)
        self.assertEqual(self.exam.get_problem(ind_dst),prob_org)
        self.assertEqual(self.exam.get_problem(ind_dst-1),prob_dst)

        #dst < org
        ind_org = 5
        ind_dst = 1
        prob_org = self.exam.get_problem(ind_org)
        prob_dst = self.exam.get_problem(ind_dst)
        self.assertEqual(self.exam.move_problem(ind_org,ind_dst), 0)
        self.assertEqual(self.exam.get_problem(ind_dst),prob_org)
        self.assertEqual(self.exam.get_problem(ind_dst+1),prob_dst)

    def test_pop_problem(self):
        exam_length = self.exam.get_length()
        last_problem = self.exam.get_problem(exam_length-1)
        self.exam.pop_problem()
        self.assertEqual(self.exam.find_problem(last_problem),-1)
        self.assertEqual(self.exam.get_length(), exam_length-1)

    def test_copy(self):
        exam_copy = self.exam.copy()
        self.assertFalse(exam_copy == self.exam)
        self.assertEqual(exam_copy.as_string(), self.exam.as_string())

    def test_check_index(self):
        self.assertFalse(self.exam.check_index(-1))
        self.assertFalse(self.exam.check_index(self.exam.get_length()))
        self.assertTrue(self.exam.check_index(0))
        self.assertTrue(self.exam.check_index(self.exam.get_length()-1))

    def test_as_string(self):
        ex = Exam("Exam", [1,1,1],ProblemSet("",self.problemA,self.problemB,self.problemC))
        points = ' '.join([str(i) for i in ex.get_points()])
        comp_str = "Exam" + "\n" + points + '\n' + self.problemA.as_string() + "\n" 
        comp_str += self.problemB.as_string() + "\n" + self.problemC.as_string() + "\n"
        self.assertEqual(ex.as_string(),comp_str)

    def test_save_load(self):
        self.exam.save("deleteme")
        load_set = Exam()
        load_set.load("deleteme")
        self.assertEqual(self.exam.as_string(),load_set.as_string())

    def test_consolidate(self):
        test = Exam()
        #test is easy if we eliminate the name otherwise we have to do a lot of str manip
        self.exam.set_name("")
        test.consolidate(self.exam,self.exam,self.exam)
        test_string = '\n' + ' '.join([str(i) for i in (self.exam.get_points()*3)])
        test_string += super(Exam,self.exam).as_string().rstrip() * 3 + '\n'
        self.assertEqual(test.as_string(),test_string)
        
    def test_txt(self):
        #self.exam.as_text_file("tester")
        pass


if __name__ == "__main__" : unittest.main()
