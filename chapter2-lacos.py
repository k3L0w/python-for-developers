#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Estruturas de repetição#
#As estruturas de repetição são conhecidas como laços (loop), 
#Geralmente, os laços são utilizados para executar determinados trechos de códigos.

# Laço: For
# . o For é o mais usado no Python.
# . o For aceita sequências estáticas e também sequências geradas por iteradores.

# Iteradores
# Iteradores -> são estruturas que permitem iterações.
# Interações -> acessos a itens de uma coleção de elementos de forma sequencial.

# Cláusula break e continue
# 'break' interrompe o laço e 'continue' passa para a próxima iteração.
# o bloco de código dentro de 'else' sempre será executado no final, exceto
# quanto houver a cláusula 'break' antes.

# Sintaxe Laço for

"""
for <referência> in <sequencia>:
    <bloco de código>
    continue
    break
else
    <bloco de código>
"""

# Soma de 0 a 19
s = 0

print()
for x in range(0, 3):
    s = s + x
print(s)
print()
