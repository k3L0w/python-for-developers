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
for x in range(0, 100):
    s = s + x
    print(s) #Apresenta a soma de cada item do interador(range).
print(" -------------------")
print("[", 'SOMA TOTAL =', s, "]") #Exibe o resultado de todos os itens do interador(range).
print(" -------------------")
print()

"""
É importante salientar que o interador(m, n, p) é muito importante em laços (loop),
pois sempre retornará uma lista de inteiros, um de item de cada vez.
Onde:
m -> inicio
n -> fim
p -> passos
"""
