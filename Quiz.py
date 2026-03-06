import random #embaralha pergunta
import time #tempo para resposta
from datetime import datetime #colocar data que nosso projeto foi feito

print("Bem-vindo ao Quiz!")
input("pressione Enter para coemçar...")

perguntas= ["per1","per2","per3","per4","per5","per6"]

random.shuffle(perguntas)
print (perguntas)