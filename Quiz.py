import random #embaralha pergunta
import time #tempo para resposta
from datetime import datetime #colocar data que nosso projeto foi feito

print("Bem-vindo ao Quiz Sobre Python!")
input("Pressione Enter para começar...")

perguntas = [
[
"Qual função mostra algo na tela em Python?", #pergunta
"A) input",
"B) print",
"C) if",
"D) for",
"B" #Resposta correta
],

[
"Qual função recebe dados do usuário?",
"A) print",
"B) input",
"C) random",
"D) time",
"B" #Resposta correta
],

[
"O que usamos para criar uma condição em Python?",
"A) if",
"B) for",
"C) print",
"D) import",
"A" #Resposta correta
],

[
"O que usamos para repetir algo várias vezes?",
"A) if",
"B) else",
"C) for",
"D) input",
"C" #Resposta correta
],

[
"Qual biblioteca usamos para embaralhar listas?",
"A) time",
"B) random",
"C) datetime",
"D) math",
"B" #Resposta correta
],

[
"PERGUNTA?",
"A) ",
"B) ",
"C) ",
"D) ",
"" #Resposta correta
],

[
"PERGUNTA?",
"A) ",
"B) ",
"C) ",
"D) ",
"" #Resposta correta
],

[
"PERGUNTA?",
"A) ",
"B) ",
"C) ",
"D) ",
"" #Resposta correta
],

[
"PERGUNTA?",
"A) ",
"B) ",
"C) ",
"D) ",
"" #Resposta correta
],

[
"PERGUNTA?",
"A) ",
"B) ",
"C) ",
"D) ",
"" #Resposta correta
],
]

random.shuffle(perguntas) #embaralha as perguntas

for pergunta in perguntas:
    for linha in pergunta[:5]: # mostra só pergunta e alternativas
        print(linha)

    resposta = input("Resposta: ").upper() #Recebe a resposta
    print()