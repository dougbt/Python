'''faça um programa que pergunte quanto voce ganha por hora eo numero de horas trabalhadas no mes.
calcule e mostre o total do seu salario no referido mes,
sabendo-se que são descontados 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:

a. salario bruto
b. quanto pagou ao inss
c. quanto pagou ao sindicato
d. o salario liquido
calcule os descontos e o salario liquido, conforme a tabela abaixo:
f. + salario bruto:RS
g. - IR(11%):RS
h. - INSS(8%):RS
i. -sindicato (5%):RS
   = SALARIO LIQUIDO:RS'''

def recebe():
    din_hora=float(input('Digite quanto você ganha por hora: '))
    trab_hora=int(input('Digite quantas horas você trabalhou esse mês: '))
    return din_hora, trab_hora

def bruto(din_hora, trab_hora):
    brut = din_hora * trab_hora
    return brut

def impostos(brut):
    ir = (brut*0.11)
    inss = (brut*0.08)
    sind = (brut*0.05)
    return brut, ir, inss, sind

def liquido(brut, ir, inss, sind):
    liq = (brut - ir - inss - sind)
    return liq

def imprim(brut, ir, inss, sind, liq):
    print('o salário bruto é R${}'.format(brut))
    print('o desconto do ir é R${}'.format(ir))
    print('o desconto do inss é R${}'.format(inss))
    print('o desconto do sind é R${}'.format(sind))
    print('o seu salário liquido é R${}'.format(liq))
    return

#Main

salario, horario = recebe()
salario_bruto = bruto(salario, horario)
salario_bruto, imposto_renda, taxa_inss, sindicato = impostos(salario_bruto)
salario_liquido = liquido(salario_bruto, imposto_renda, taxa_inss, sindicato)
imprim(salario_bruto, imposto_renda, taxa_inss, sindicato, salario_liquido)
