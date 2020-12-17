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
    print()
    print('CUIDADO COM VENTOS! Temperaturas abaixo de zero (0 )oferecem risco a vida!')
    print('Em temperaturas de -29° com ventos a 16km/h, a sensação térmica seria equivalente a -44°C')
    print('Em temperaturas de -29, com ventos a 40Km/h, a sensação térmica seria equivalente a -66°C')
    print()
    print('CUIDADO COM A ÁGUA, a sensação térmica pode ser ainda pior!!!.')
    print('Um mergulho em um lago a -5°C pode causar hipotermia em menos de 30 minutos.')
    print()
elif 0 <= temp <= 20:
    print('Frio')
elif 21 <= temp <= 25:
    print('normal')
elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente!')
print()

