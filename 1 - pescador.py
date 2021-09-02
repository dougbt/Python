'''joão Papo-de-pescador, homem de bem, comprou um microcomputador para controlar o rendimento diario de seu trabalho. toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de SP(50 quilos) deve pagar uma mulda de R$4,00 por quilo excedente. joão precisa que voce faça um programa que leia a variavel peso(peso de peixes) e calcule o excesso. gravar na variavel excesso a quantidade de quilos além do limite e na variavel multa o valor da multa que joao devera pagar. imprima os dados do programa com as mensagens adequadas.'''

def ler():
    peso = float(input('Digite o peso dos peixes: '))
    return peso

def calc(peso):
    if peso>50:
        excesso=peso-50
        multa=excesso*4
    else:
        excesso=0
        multa=0
    return excesso, multa

def imprim(peso, excesso, multa):
    print('O peso do peixe é {}Kg '.format(peso))
    if multa!=0:
        print('O excesso foi {}Kg '.format(excesso))
        print('Excedeu o permetido e a multa é de R${} '.format(multa))
    else:
        print('Não teve excedente')

#Main

ppeixe = ler()
ex, multa = calc(ppeixe)
imprim(ppeixe,ex,multa)
