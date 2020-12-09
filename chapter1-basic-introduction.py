#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Strings no python são definidas por aspas duplas ("") ou simples ('').
#vide:
#>>> "digite_texto_aqui"
# ou
#>>> 'digite_texto_aqui'

#Função .upper()
#Esta função retorna CAIXA ALTA para as strings.
#vide:
#>>> "texto".upper()
#TEXTO
#>>>

#Função len()
#Retorna a quantidade de caracteres em uma ou mais strings.
#vide:
#>>> len("A função len irá retornar a quantidade de caracteres, incluindo os espaços que esta string possue.")
#98
#>>>

#Função str
#Converte números em strings.
#vide:
#>>>len(str(123))
#123
#>>>len('123')
#123
#>>>

#Função int
#Converte números (não inteiros) em números inteiros.
#int(123,45)
#123
#>>>

#Variáveis no Python
#É de suma importância o uso de variáveis, pois é um nome que se atribui a um objeto.
#Variáveis podem ser utilizadas para armazenar dados, isso torna o código mais legível e muito mais produtivo.
#Vide:
#Variável pode armazenar texto:
#name = "Arham Om Talsania" #Talsania, indiano de 6 anos, reconhecido como o programador mais jovem do mundo.
#>>> name
#Arham Om Talsania

#Utilizando funções com strings
#>>>name = "Arham Om Talsania"
#>>>len(name)
#17
#>>>

#Variável pode armazenar números:
#>>> a = 7
#>>> b = 5
#>>> a * b
#35

#Função print no Python
#woman = "Aninha"
#print(woman)
#Aninha

#Listas no Python
#Listas no Python são definidas pelos caracteres []. 
#Vide:
#>>>nomes = ['Antonio', 'Divina', 'Elitania', 'Elisangela', 'Zirlandia', 'Rute', 'Sara', 'Raquel', 'Kesia']
#>>>print(nomes)
#['Antonio', 'Divina', 'Elitania', 'Elisangela', 'Zirlandia', 'Rute', 'Sara', 'Raquel', 'Kesia']
#

#Outro exemplo de lista
#>>> sena = [5, 7, 11, 13, 45, 57]
#>>> print(sena)
#[5, 7, 11, 13, 45, 57]

#>>> len(sena)
#6

#>>> len(str(sena)) #nesse caso, str converte a lista em strings.
#22

#>>> organizando uma lista (ordem crescente)
#>>> sena.sort()
#>>> sena
#[5, 7, 11, 13, 45, 57]

#>>> organizando uma lista (ordem decrescente)
#>>> sena.reverse()
#[57, 45, 13, 11, 7, 5]

#>>> adicionando item a lista
#>>> sena.append(15)
#>>> sena
#[5, 7, 11, 13, 45, 57, 15]

#Agora é só utilizar a função .sort() para organizar por ordem crescente ou decrescente com .reverse()
#Organizando com .sort()
#>>> sena.sort()
#>>> sena
#[5, 7, 11, 13, 15, 45, 57]

#Organizando com .reverse()
#>>> sena.reverse()
#>>> sena
#[57, 45, 15, 13, 11, 7, 5]

