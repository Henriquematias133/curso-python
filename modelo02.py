# Vamos começar criando uma classe chamada carro
# Uma classe é um molde ou planta que define comoo os objetos dessa classe serão
# Ela define o que um objeto pode fazer(os metodos) e o que eles tem(os atributos)

class Carro:
    #a classe carro tem dois atributos: "marca" e "modelo" , e um metodo:acelerar.
    # o metodos especial __init__ é o que chama quando crismos um obejeto da classe
    # Ele inicializa os atributos do objeto(marca e modelo)
    def __init__(self,marca,modelo,cor):
        #os atributos do obejto serão definidos dentro do init
        # o self refere-se ao proprio objeto que está sendo criado
        self.modelo = modelo # atributo que armazena o modelo
        self.marca = marca # atributo que armazena o modelo
        self.cor = cor

    # esse é o metodo que define o comportamneto do objeto, aqui estamos falando o que de fato o carro faz

    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando")

    def parar(self):
        print(f"O {self.marca} {self.modelo} parou")
    
    def direita(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou para direita")
    
    def esquerda(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou para esquerda")
    

carro1 = Carro("Fusca","1984","Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.parar()
carro1.direita()
carro1.esquerda()



