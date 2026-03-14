import random 
import time 
from datetime import datetime 

print("Bem-vindo ao Quiz Sobre Python!")
input("Pressione Enter para começar...")
print()
print("Digite apenas a letra da resposta (A, B, C ou D).")
print()

perguntas = [
[
"Qual função mostra algo na tela em Python?", 
"A) input",
"B) print",
"C) if",
"D) for",
"B" 
],

[
"Qual função recebe dados do usuário?",
"A) print",
"B) input",
"C) random",
"D) time",
"B" 
],

[
"O que usamos para criar uma condição em Python?",
"A) if",
"B) for",
"C) print",
"D) import",
"A" 
],

[
"O que usamos para repetir algo várias vezes?",
"A) if",
"B) else",
"C) for",
"D) input",
"C" 
],

[
"Qual biblioteca usamos para embaralhar listas?",
"A) time",
"B) random",
"C) datetime",
"D) math",
"B" 
],

[
"Qual símbolo usamos para fazer um comentário em Python?",
"A) //",
"B) #",
"C) -",
"D) **",
"B" 
],

[
"Qual palavra usamos para criar uma função em Python?",
"A) function",
"B) create",
"C) def",
"D) func",
"C" 
],

[
"Qual tipo de dado representa números inteiros em Python?",
"A) string",
"B) float",
"C) int",
"D) bool",
"C" 
],

[
"Qual valor representa verdadeiro em Python?",
"A) true",
"B) yes",
"C) 1",
"D) True",
"D" 
],

[
"Qual estrutura usamos para repetir enquanto uma condição for verdadeira?",
"A) while",
"B) repeat",
"C) for",
"D) loop",
"A" 
],
]

random.shuffle(perguntas) 
placar = 0
tentativas = 0

for pergunta in perguntas:
    for linha in pergunta[:5]: 
        print(linha)

    print()

    resposta = input("Resposta: ").upper()  
    tentativas += 1

    print()

    if resposta == pergunta[5]:
        print("Acertou!")
        placar += 1
    else:
        print("Errou! A resposta correta é:", pergunta[5]) 
    print()
    print("Próxima pergunta...")
    time.sleep(2)

    
print("Quiz finalizado!") 
print("Você acertou", placar, "de", tentativas, "perguntas.")

data = datetime.now()
print("Data do quiz:", data.strftime("13/03/2026"))
