#makefile: tests class of exampkg/lib using tests from exampkg/lib/test

P := python3
F := -v

test: test/Test_Problem.py test/Test_ProblemSet.py

test/Test_Problem.py: Problem.py
	${P} test/Test_Problem.py ${F}
	echo $?

test/Test_ProblemSet.py: ProblemSet.py
	${P} test/Test_ProblemSet.py ${F}
	echo $?
