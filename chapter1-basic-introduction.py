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
#'TEXTO'
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
#int(123.45)
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

#Indices em listas
#Importante salientar que o índice se inicia em 0.
#>>> sena
#[1, 3, 8, 12, 12, 23, 33, 48]
#>>> print(sena[0])
#1 #Neste exemplo, o número 1 é o índice '0' da lista, o primeiro da lista, o indice inicia-se em '0'.

#Outros exemplos de índices
#>>> print(sena)
#[3, 8, 12, 12, 23, 33, 48]
#>>> print(sena[-1])
#48
#>>> print(sena[-2])
#33
#>>> print(sena[-3])
#23
#>>> print(sena[-4])
#12
#>>> print(sena[-5])
#12
#>>> print(sena[-6])
#8
#>>> print(sena[-7])
#3

#Deletar um item da lista, utilizando pop.
#>>>sena
#[1, 3, 8, 12, 12, 23, 33, 48]
#>>> sena.pop(0)
#1
#>>> print(sena)
#[3, 8, 12, 12, 23, 33, 48]

#Dicionários em Python
#Semelhante a listas, dicionários são acessados utilizando-se chaves, ao inves de índice.
#Chaves nos dicionários podem ser string ou números.
#sintaxe:
#>>> {} #dicionário vazio.

#>>> participant = {'name':'aninha','city':'Goiania','age':18,'numbers':[7,45,120]}
#>>> participant
# {'name': 'aninha', 'city': 'Goiania', 'age': 18, 'numbers': [7, 45, 120]}
#>>> 

# Onde: 
# . A chave 'name' aponta o valor 'aninha' (um objeto do tipo 'string').
# . A chave 'city' aponta para o valor 'Goiania' (um objeto do tipo 'string').
# . A chave 'age' aponta para o valor 18 (um objeto do tipo número inteiro).
# . A chave 'numbers' aponta para o valor [7, 45, 120] (uma lista de três números).

# Verificando o conteúdo de chaves individualmente
##>>> print(participant['name'])
#aninha
#>>> print(participant['age'])
#18
#>>> print(participant['city'])
#Goiania
#>>> print(participant['numbers'])
#[7, 45, 120]
#>>> 

# Uso lista ou dicionário?
# . lista -> para sequência ordenada de itens.
# . dicionário -> para associar valores a chaves para achá-las eficientemente (pela chave).

# Listas e dicionários são MUTÁVEIS, podem ser alterados em sua composição.
#>>> participant['language'] = 'English'
#>>> participant
#{'name': 'aninha', 'city': 'Goiania', 'age': 18, 'numbers': [7, 45, 120], 'language': 'English'}
#>>> 

# Assim como nas listas, a função len() retorna os pares de chave-valor que um dicionário contém.
# Vide:
# >>> len(participant)
# 5

# Deletar um item do dicionário:
#>>> participant.pop('numbers')   
# [7, 45, 120]
#>>> print(participant)
# {'name': 'aninha', 'city': 'Goiania', 'age': 18, 'language': 'English'}
#>>> len(participant)
# 4
#>>>

 # Mudar o valor associado a uma chave no dicionário:
 # participant['age'] = 19
 # print(participant['age'])
 # 19
 #>>> participant
#{'name': 'aninha', 'city': 'Goiania', 'age': 19, 'language': 'English'}


