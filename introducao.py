''' a proxima linha mostra meu nome! '''

print("Henrique Matias Da Silva")

print("Meu nome é: Henrique. \nMeu curso é: Python")

"""
Trabalhando com tipificação e variaveis
"""

nome = "Henrique" #string
sobrenome = "Matias"
idade = 21 #integer
altura = 1.73 #float
bermuda = False #boolean

print(nome + " " + sobrenome + " tem " + str(idade))

print(idade + 2)

textoVariasLinhas = ''' 
Operadores
soma +
Subtração - 
divisão /
potencia ^
exponenciação **
multiplicação *
'''

print(textoVariasLinhas)


# Detalhamento strings e usando formato
nomeCompleto = "Henrique Matias Da Silva"
inicio = 5
fim = inicio + 6
print(nomeCompleto[inicio:fim])


qNome = input("Insira seu nome :")
qSobrenome = input("Insira seu sobrenome :")
print( "Seu nome é:" + qNome +" " + qSobrenome)




