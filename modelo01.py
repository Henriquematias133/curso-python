# Função para criar um carro com marca e modelo
def criar_carro(marca, modelo):
    return{"marca": marca,"modelo": modelo}

def acelerar(carro):
    print(f"O {carro['marca']} {carro['modelo']} está acelerando")

def parar(carro):
    print(f"O {carro['marca']} {carro['modelo']} parou")
 
#função para criar um carro com cor adicional

def criar_carro_com_cor(marca,modelo,cor):
    carro = criar_carro(marca,modelo)
    carro["cor"]= cor
    return carro

def exibir_cor(carro):
    print(f"O carro é da cor{carro['cor']}.")
    
def Virar_para_direita(carro):
    print(f"O {carro['marca']} {carro['modelo']} virou para direita")

def Virar_para_esquerda(carro):
    print(f"O {carro['marca']} {carro['modelo']} virou para esquerda")



# Criar os carros
carro1 = criar_carro("Fusca","1984")
carro2 = criar_carro("Suzuki","Jimmy")

# Acelerando e parando os carros
print(carro1["marca"]) #acessando a marca
print(carro1["modelo"]) #acessando o modelo

#criando carro com cor

carro3 = criar_carro_com_cor("Toyota", "Etios", "Branco")
print(carro3["marca"])
print(carro3["modelo"])
print(carro3["cor"])
exibir_cor(carro3)

print('---------------------Corrida-------------------------')
acelerar(carro3)
parar(carro3)
print(carro2["marca"])
print(carro2["modelo"])
acelerar(carro2)
parar(carro2)
Virar_para_direita(carro2)
Virar_para_esquerda(carro2)

