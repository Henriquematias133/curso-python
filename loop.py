# --------------------- loop: For
palavra = "sucesso"
contador = 0
for letra in palavra:
    print(str(contador) + " - " + letra)
    contador = contador + 1 

cidades = ['São Paulo','Barueri','Poá','Manaus'] 

#print(cidades[0])

for cidade in cidades : 
    print(cidade)
# - ------------------- loop: While
botaoExecutar = True
contador = 0
while botaoExecutar:
    print(contador)
    contador = contador + 1 
    if contador >= 10 :
       botaoExecutar = False

# -------------------------------- Funções

def    minhaFuncao() :
        print('lalala') 

minhaFuncao()
minhaFuncao()

cidades = ['São Paulo','Barueri','Poá','Manaus'] 
contador = 0

def minhaFuncaoMelhorada(informacao, x) :
    print( str(x) + ' - '+ informacao)


for cidadde in cidades :
    contador= contador + 1 
    minhaFuncaoMelhorada(cidade, contador)
