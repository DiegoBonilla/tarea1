#!/usr/bin/env python
# -*- coding: utf-8 -*-
# primos.py: devuelve todos los números primos hasta n

def raizCuadrada(x):
	r = x
	t = 0
	while (t != r):
		t = r
		r = (x/r + r)/2
	return r

def primos():
  '''Devuelve todos los números primos hasta n.
  '''

  nro = raw_input('Ingrese un numero mayor a 1: ')
  n = int(nro)
  
  if n > 1:
	primos = [2]

	for k in range(3, n):
	  for i in range(len(primos)):    
		if k%primos[i]==0: break
	  
	  if i==len(primos)-1: #solo si no es multiplo de los actuales primos
		primos.append(k)        
	
	i = 0
	while (i < len(primos)):
		print primos[i]
		i += 1
	
	
  
  