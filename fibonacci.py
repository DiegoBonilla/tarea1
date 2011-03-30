#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fibonacci.py: Devuelve  los números de la serie de Fibonacci hasta n

def fibo(n):
  if n == 0 :
	return 0
  elif n == 1:
	return 1
  else:
	return fibo(n-1) + fibo(n-2)
	
	
def fibonacci():
  '''Devuelve  los números de la serie de Fibonacci hasta n.
  '''
  
  nro = raw_input('Ingrese la cantidad de conejos: ')
  n = int(nro)
  
  if n < 0:
    print "La cantidad de conejos debe ser mayor o igual a 0."
  else:
	print "Sucesion de Fibonacci :"
	while (n >= 0):
	  print "n = " + str(n) + " --> " + str(fibo(n))
	  n -= 1
  
 