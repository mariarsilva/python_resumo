#!/usr/bin/env python3 #informa que o ambiente é o python3

"""python é uma linguagem tipada, logo não precisa ficar nomeando 'int', 'char', etc.
exceto se você quiser fazer um cast, que é mudar o tipo de uma variavel. Ex: de int para char."""

#para ver o tipo de uma variavel:

var1 = 10
var2 = 'blablabla'
var3 = 5.873
var4 = "etcetcetc"

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#Exibindo uma classe sem tipo
print(type(print()))

#OBS:para exibir esses valores digite no terminal 'python3 programa.py' na pasta do arquivo

#print = saida de dados
#input = entrada de dados

nome1 = input('Você é... ')
print('uepaaaa')
print(nome1)

#fprint

nome2 = input('Diz aê teu nome: ')
print(f'Duvido que seu nome seja esse, {nome2}!')

#cast =  converter um tipo de dados
valor = input('me diga um numero ai: ')
valor2 = input('apois me diga outro numero rs: ')
soma_complexa = valor + valor2
print(f'O valor dessa super soma: {soma_complexa} :-O OMG!!!!')

#and / or / not
