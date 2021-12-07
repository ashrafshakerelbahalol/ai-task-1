
 #q1
import aima.utils
import aima.logic
  clauses=[]
  clauses.append(aima.utils.expr("Carrot(x) & Orange(y) & Color(x,y)"))
  clauses.append(aima.utils.expr("(Person(x) & Carrort(y) & Like(x,y)) ==> Vegetrian(x)"))
  clauses.append(aima.utils.expr("(Student(x) & Pass(y)) ==> study_hard(x)"))
  KB = aima.logic.FolKB(clauses)
  KB.tell(aima.utils.expr("enemy(x,y) ==> (hate(x,y) & fight(x,y))"))
if __name__ == "__main__": main()  
 #q2
  clauses=[]
  clauses.append(aima.utils.expr("Maria(x) & Programable_book(y) & Read(x,y,z) & peterlucas(z)"))
  clauses.append(aima.utils.expr("Person(x) & shoping (y) & Like(z) ==> Girl(x)"))
  person_who = KB.ask(aima.utils.expr("Person(x)")
  kb.tell(aima.utils.expr("(Kikire(x) & City(y) & hate(x,y)) ==> Crowd(y) & big(y)" ))
 #q3
  clauses=[]
  clauses.append(aima.utils.expr("( hate(x,y) & hate(y,x)) <==> (enemy(x,y) & enemy(y,x))"))
  clauses.append(aima.utils.expr("(p(x) ==> q(x) ==> r(x)"))
  