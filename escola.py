tipoEscola = input("Tipo do Colegio: \n [1]Publico \n [2] Particular")
nota01 = imput("Qual a nota do 1º Bimestre: ")
nota02 = imput("Qual a nota do 2º Bimestre: ")
nota03 = imput("Qual a nota do 3º Bimestre: ")
nota04 = imput("Qual a nota do 4º Bimestre: ")
freqAluno = imput("Qual a frequencia: ")
nomeAluno = imput("Nome do aluno: ")
mediaAluno = (int(nota01) + int(nota02) + int(nota03) + int(nota04)) / 4

print("O aluno(a) " + nomeAluno + "possui a média de :" + str(mediaAluno))