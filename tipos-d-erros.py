#!/usr/bin/python
# -*- coding: UTF-8 -*-

#---------
#TypeError
#---------
#Vide exemplo:
#>>> len(123456)
#Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#TypeError: object of type 'int' has no len()
#>>>


#----------
#nameError
#----------
#Vide exemplo:
#>>> city = "Sao Paulo"
#>>> citi
#Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#NameError: name 'citi' is not defined
#>>>

#----------
#IndexError
#----------
#>>> sena
#[5, 7, 11, 13, 15, 45, 57]
#>>> print(sena[7])
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: list index out of range


#--------------
#AttributeError
#--------------
#>>> l1 = ['lista']
#>>> l1
#['lista']
#>>> l1.upper()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'list' object has no attribute 'upper'

#--------
#KeyError
#--------
#>>> participant['cidade']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'cidade'
#>>>

