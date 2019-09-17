#!/usr/bin/env python3

import unittest
from lib.Problem        import Problem
from lib.ProblemSet     import ProblemSet

class ProblemSetTest(unittest.TestCase):

    def setUp(self):
        self.name = "Problem_Set"
        self.pset = ProblemSet(self.name)
        self.pset.test_fill_quotes()
        self.pset.test_fill_math(10)
        self.pset.test_fill(10)

        self.problemA = Problem("Question A","Answer A")
        self.problemB = Problem("Question B","Answer B")
        self.problemC = Problem("Question C","Answer C")

    def test_get_name(self):
        self.assertEqual(self.name, self.pset.get_name())

    def test_set_name(self):
        self.pset.set_name("My Problem Set")
        self.assertEqual("My Problem Set" , self.pset.get_name())

    def test_add_problem(self):
        self.pset.add_problem(self.problemA)
        self.assertEqual(self.pset.get_problem(self.pset.get_length()-1),self.problemA)

    def test_find_problem(self):
        self.assertEqual(self.pset.find_problem(self.problemA), -1)
        self.pset.add_problem(self.problemA)
        self.pset.add_problem(self.problemB)
        self.pset.add_problem(self.problemC)
        ind_probA = self.pset.find_problem(self.problemA)
        ind_probB = self.pset.find_problem(self.problemB)
        ind_probC = self.pset.find_problem(self.problemC)
        self.assertEqual(self.pset.get_problem(ind_probA),self.problemA)
        self.assertEqual(self.pset.get_problem(ind_probB),self.problemB)
        self.assertEqual(self.pset.get_problem(ind_probC),self.problemC)

    def test_remove_problem(self):
        self.assertEqual(self.pset.remove_problem(self.problemA),-1)

        p = self.pset.get_problem(0)
        self.assertEqual(self.pset.remove_problem(p),0)
        self.assertEqual(self.pset.find_problem(p), -1)

    def test_replace_problem(self):
        p = self.pset.get_problem(0)
        self.pset.replace_problem(0,self.problemA)
        self.assertEqual(self.pset.find_problem(p), -1)
        self.assertEqual(self.pset.find_problem(self.problemA), 0)

    def test_insert_problem(self):
        p = self.pset.get_problem(5)
        self.pset.insert_problem(5,self.problemA)
        self.assertEqual(self.pset.get_problem(5),self.problemA)
        self.assertEqual(self.pset.get_problem(6),p)

    def test_swap_problem(self):
        self.assertEqual(self.pset.swap_problem(-1,1),-1)
        self.assertEqual(self.pset.swap_problem(0,0),-1)
        self.assertEqual(self.pset.swap_problem(1,-1),-1)

        p0 = self.pset.get_problem(0) #problem in position zero orginally
        p1 = self.pset.get_problem(1) #problem in position one  orginally
        self.assertEqual(self.pset.swap_problem(0,1),0)
        self.assertEqual(self.pset.get_problem(0),p1) #p1 should be in pos 0
        self.assertEqual(self.pset.get_problem(1),p0) #p0 should be in pos 1

    def test_move_problem(self):
        #dst > org
        ind_org = 0
        ind_dst = 10
        prob_org = self.pset.get_problem(ind_org)
        prob_dst = self.pset.get_problem(ind_dst)
        self.assertEqual(self.pset.move_problem(ind_org,ind_dst), 0)
        self.assertEqual(self.pset.get_problem(ind_dst),prob_org)
        self.assertEqual(self.pset.get_problem(ind_dst-1),prob_dst)

        #dst < org
        ind_org = 12
        ind_dst = 1
        prob_org = self.pset.get_problem(ind_org)
        prob_dst = self.pset.get_problem(ind_dst)
        self.assertEqual(self.pset.move_problem(ind_org,ind_dst), 0)
        self.assertEqual(self.pset.get_problem(ind_dst),prob_org)
        self.assertEqual(self.pset.get_problem(ind_dst+1),prob_dst)

    def test_pop_problem(self):
        pset_length = self.pset.get_length()
        last_problem = self.pset.get_problem(pset_length-1)
        self.pset.pop_problem()
        self.assertEqual(self.pset.find_problem(last_problem),-1)
        self.assertEqual(self.pset.get_length(), pset_length-1)

    def test_copy(self):
        pset_copy = self.pset.copy()
        self.assertFalse(pset_copy == self.pset)
        self.assertEqual(pset_copy.as_string(), self.pset.as_string())

    def test_consolidate(self):
        p1 = ProblemSet("",self.problemA,self.problemB)
        p2 = ProblemSet("",self.problemB,self.problemC)
        p3 = ProblemSet("",self.problemC,self.problemA)
        test_string = p1.as_string().rstrip() +p2.as_string().rstrip()  +  p3.as_string()
        p1.consolidate(p2,p3)
        self.assertEqual(p1.as_string(), test_string)


    def test_check_index(self):
        test = ProblemSet("",self.problemA,self.problemB,self.problemC)
        self.assertFalse(test.check_index(-1))
        self.assertFalse(test.check_index(test.get_length()))
        self.assertTrue(test.check_index(0))
        self.assertTrue(test.check_index(test.get_length()-1))

    def test_as_string(self):
        ps = ProblemSet("ProblemSet")
        ps.add_problem(self.problemA)
        ps.add_problem(self.problemB)
        ps.add_problem(self.problemC)
        comp_str = "ProblemSet" + "\n" + self.problemA.as_string() + "\n" 
        comp_str += self.problemB.as_string() + "\n" + self.problemC.as_string() + "\n"
        self.assertEqual(ps.as_string(),comp_str)

    def test_save_load(self):
        self.pset.save("deleteme")
        load_set = ProblemSet()
        load_set.load("deleteme")
        self.assertEqual(self.pset.as_string(),load_set.as_string())

    def test_txt(self):
        self.pset.as_text_file("tester")


if __name__ == "__main__" : unittest.main()
