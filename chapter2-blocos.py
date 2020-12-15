#!/usr/bin/python
# -*- coding:UTF-8 -*-

# As indentações são importantes em códigos Python.
# São utilizados para delimitar blocos de códigos.
# É considerado uma 'boa prática' utilizar um único padrão nos códigos,
# Endentação ou espaços (4).

"""
Vide exemplo:

----------------------
#!/usr/bin/python
# -*- coding:UTF-8 -*-

PROGRAMA
Instruções
Enquanto Condição:
    instruções
    Se condição:
        instruções
    Senão:
        instruções
instruções
----------------------
Esse é um exemplo de uma estrutura de um programa escrito em Python

Obs.: a linha anterior sempre termina com (:), representa uma estrutura de controle do Python,
ou declação de uma nova estrutura (função, por exemplo)
"""

#Vide

# Para i na lista 234, 654, 378, 798:

print()
for i in [234, 654, 378,798]:
    # Se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:
        # Imprime...
        print(i, '/ 3 =', i / 3)
print()

# Vide outro exemplo

# para s na lista:
# 1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60

for s in [1, 2, 3, 4, 6, 7, 8, 9, 
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60]:
    # Novamente, se o resto em s dividido por 3 for 0:
    if s % 3 == 0:
        # Imprime...
        print(s, '/ 3 = ', s / 3)
print()