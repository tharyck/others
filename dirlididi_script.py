#@Author: Tharyck Vasconcelos

#Copie o seu log do dirlididi, garantindo a data e o horario desejado. 
#(CUIDADO: o dirlididi trabalha em GMT 0, lembre de sempre add 3 hrs a mais)
#crie um arquivo chamado log.txt (de preferencia no sublime), cole o seu log e salve no mesmo diretorio que esse script.
#Rode o sript.
#Sera gerado um arquivo de saida chamado notas.txt, que contem email do aluno e a sua respectiva nota.
#me pague uma cerveja por ter economizado horas corrigindo um lab!


#Se encontrar algum erro, ou quiser editar o codigo, fique avontade!

import collections
ref_arquivo = open("log.txt","r")
linha = ref_arquivo.readline()
turma = []
final = []

#Array com o key das questoes
questoes = []

#pega a quantidade de questoes e os keys de cada
for i in range(int(raw_input("Informe a quantidade de questoes: "))):
	questoes.append(raw_input("Informe o Key da " + str(i + 1) + " Questao: "))


#filtra as questoes que passaram
while linha:
	#pega cada linha do arquivo e separa
    valores = linha.split()

    #pega apenas as questoes que passaram
    if('true' in linha):
        #testa se a questao que passou e questao do lab
        if(valores[2] in questoes):
            novalinha = valores[1] + ' ' + valores[2]
            #testa se a questao passou mais de uma vez
            if(novalinha not in turma):
                turma.append(novalinha)
    linha = ref_arquivo.readline()

#conta a quantidade de questoes que cada aluno acertou e transforma para uma "nota"
for i in range(len(turma)):
    contador = 0
    valores = turma[i].split()
    for j in range(len(turma)):
        valor = turma[j].split()
        if(valores[0] == valor[0]):
            contador+=1

	#Nota
    nota = (10.0/len(questoes))*contador

    #alunonota = email do aluno + nota do lab
    alunoNota = valores[0] + ' ' + str(nota)
    if(alunoNota not in final):
        final.append(alunoNota)

#escreve no arquivo de saida notas.txt
ref_arquivo = open("notas.txt", "w")
#ordena a turma antes de escreve na saida
turma = sorted(final)
#escreve na saida
for i in range(len(turma)):
   ref_arquivo.writelines(turma[i] + '\n')

#fehca o arquivo notas.txt
ref_arquivo.close()