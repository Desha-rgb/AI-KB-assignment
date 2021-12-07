# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:10:41 2021

@author: ELGOHARY
"""
# 1- Write python code, accompanied with equivalent English statements, that represent the following facts:
 (1)color(carrots, orange).
 carrots color is orange
 (2) likes(Person, carrots):-vegetarian(Person). 
 person likes carrots if person is vegetarian
 (3) pass(Student) :- study_hard(Student). 
student pass if student study hard 
 (4) ?- pass(Who).
 who will pass
 (5) ?- teaches(professor, Course). 
 which professor teaches Course
 (6) enemies(X, Y) :- hates(X, Y), fights(X, Y).
 if X and Y are enemies ,then X hates Y and X fights Y
 
  # 2- For below English sentences write applicable Python code that represents facts, rules & goals:
 (1) Maria reads logic programming book by author peter lucas. 
 reads(Maria, logicprogrammingbook) :- author(peter_lucas)
 (2) Anyone likes shopping if she is a girl. 
 likes (anyone, shopping) :- girl(anyone)
 (3) Who likes shopping? 
 ?- likes(x,shopping)
 (4) kirke hates any city if it is big and crowdy.
 hates(kirka):-city(big,crowdy)

 
 
 # 3- There are flaws in the following clauses, find them, correct them, and write python code that implements them 
 (1) hates(X,Y), hates(Y,X) :- enemies(X, Y) 
     hates(X,Y) ^ hates(Y,X) :- enemies(X, Y) 
 (2) p(X):-(q(X):-r(X)).
     (p(X):-q(X) ^ q(x):-r(X))):-p(x):-r(x) .
        

 # 4- For given English statements write a python program, - Facts & Rules
 
 (1) jia is a woman. 
 (2) john is a man. 
 (3) john is healthy. 
 (4) jia is healthy. 
 (5) john is wealthy. 
 (6) anyone is a traveler if he is healthy and wealthy.
(7) anyone can travel if he is a traveler. 
- Goals. 
(1) Who can travel? 
(2) Who is healthy and wealthy?
  

#The python program:

woman(jane).
man(john).
healthy(john).
healthy(jane).
wealthy(john).
traveller(x):- traveller(x,healthy,wealthy).
travel(x):-travel(x,traveller).
?-travel(who).
?-healthy(x),wealthy(x).       
        
