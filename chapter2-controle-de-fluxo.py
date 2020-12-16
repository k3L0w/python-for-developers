#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Validar estruturas de dados envolve o uso de instruções condicionais.

"""
Exemplo:
if <condição>: #condição -> sentença que possa ser avaliada como verdadeira ou falsa.
    <bloco de código> #sequência de linhas de comando. 
elif <condição>:
    <bloco de código>
elif <condição>:
    <bloco de código>
else:
    <bloco de código>
"""

temp = int(input('Entre com a temperatura atual: '))

if temp < 0:
    print('Congelando...')
elif 0 <= temp <= 20:
    print('Frio')
elif 21 <= temp <= 25:
    print('normal')
elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente!')
