# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:10:02 2021

@author: MosaTech
"""
import aima.utils
import aima.logic
def main():
  clauses=[]
  clauses.append(aima.utils.expr("John(x) ==> Man(x)"))
  clauses.append(aima.utils.expr("Jia(y) ==> Woman(y)"))
  clauses.append(aima.utils.expr("John(x) ==> Healthy(x)"))
  clauses.append(aima.utils.expr("John(x) ==> Weathy(x)"))
  clauses.append(aima.utils.expr("(Healthy(X) & Weathy(x)) ==> Traveler (x)"))
  clauses.append(aima.utils.expr("Traveler(x) ==> Travel(x)"))
  KB = aima.logic.FolKB(clauses)
  Treavller = KB.ask(aima.utils.expr("Traveler(x)")
  H = KB.ask(aima.utils.expr("Healthy(x) & Weathy(x)")
  print('traveller')
  print(Treavller)
  print('\n weathy and healthy')
  print(H)
if __name__ == "__main__": main()  