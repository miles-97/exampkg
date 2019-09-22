Using MakeExam.py, "problem sets" and "exams" may be created. A 
"problem set" is a collection of "problems" which consist of a
question and an answer. An "exam" is a collections of problems 
and point values assosciated with those problems.

To create a "problem set" or "exam" run:
	./setup.sh 
	python3 MakeExam.py

To be quizzed on the contents of a "problem set" or "exam":
	python3 Quizzer.py -e <examfile>
	python3 Quizzer.py -p <problemsetfile>



