#!/usr/bin/python
# -*- coding: utf-8 -*-

# Objetivo: exibir listas definidas por categorias de instrumentos musicais.
# Lista de instrumentos musicais mais comuns atualmente
instruments = ['bass', 'drums', 'guitar', 'keyboard']
print()
print('--------------------------------------')
print('* Instrumentos musicais mais comuns: *')
print('--------------------------------------')
print(instruments)
print()

print()
print("Instrumentos musicais são categorizados em três grandes grupos:")
print("1. percussão")
print("2. sopro")
print("3. cordas")

# Instrumentos de percussão
print()
percussions = ['adufe', 'afoxé', 'agogô', 'atabaque', 'batá', 'bateria', 'bloco sonoro', 'bombo', 'bongó', 'caixa Surso', 'carrilhão', 'castanhola', 'caxixi', 'ceramofone', 'chocalho', 'conga', 'cordofone', 'cuica', 'ganza', 'gongo', 'marimba', 'metalofone', 'pandeireta', 'pandeiro', 'pratos', 'reco-reco', 'repinique', 'sino', 'tambom', 'tamborim', 'tantã', 'timpano', 'triângulo', 'vibrafone', 'xequerê', 'xilofone']
print("1. Instrumentos musicais de percussão:")
print("Nesses instrumentos se obtém o som por meio da vibração de uma membrana ou superfície.")
for percussion in percussions:
    print('.', percussion)
print()

# Instrumentos de sopro (Madeira)
print()
madeiras = ['Clarinete', 'clarone', 'contrafagote', 'corne', 'didjeridu', 'fagote', 'flauta', 'flautim', 'gaita', 'gaita de foles', 'harmônica', 'oboé', 'requinta', 'saxofone']
print("2. Instrumentos musicais de sopro constituídos de madeira")
print("O som é obtido por meio da movimentação do ar nos tubos que constituem esses instrumentos")
for madeira in madeiras:
    print('.', madeira)
print()

# Instrumentos de sopro (metal)
print()
metais = ["bombardino", "clarim", "corneta", "fliscorne", "trombone", "trompa", "trompete", "tuba"]
print("2. Instrumentos musicais de sopro constituídos de metal")
for metal in metais:
    print(".", metal)
print()

# Instrumentos musicais de corda
print()
cordas = ["alaúde", "baixo", "balalaica", "bandola", "bandolim", "banjo", "berimbau", "cavaquinho", "charango", "citara", "contrabaixo", "cordofone", "guitarra", "harpa", "rabeca", "ukulele", "viola", "violão", "violino", "violoncelo"]
print("3. Instrumentos musicais de cordas")
print("Nos instrumentos de cordas, o som é obtido pela vibração de cordas percutidas ou friccionadas")
for corda in cordas:
    print(".", corda)
print()

# Instrumentos musicais de teclas são classificados como instrumentos de cordas.
print()
teclas = ["acordeão", "clavicórdio", "concertina", "cravo", "espineta", "órgão", "piano", "sintetizador", "teclado"]
print("3. Instrumentos de teclas, também se classificam como instrumentos de cordas")
for tecla in teclas:
    print(".", tecla)
print()