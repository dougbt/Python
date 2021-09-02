'''faça um programa para o calculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado(é a empresa que deposita). o salario liquido corresponde ao salario bruto menos os descontos'''

def ler():
    din_hora = float(input('Digite quanto você ganha por hora: '))
    trab_hora = int(input('Digite quantas horas você trabalhou esse mês: '))
    return din_hora, trab_hora

def bruto(din_hora,trab_hora):
    bru = din_hora*trab_hora
    print('Salário Bruto: {}*{}           : R${} '.format(din_hora,trab_hora, bru))
    return bru

def imposto(bru):
    if bru<=900:
        ir=0
        print('Imposto de Renda:           ISENTO')
        return ir

    elif bru>900 and bru<=1500:
        ir = bru*0.05
        print('(-)Imposto de Renda:  (5%)           : R${:7.2f} '.format(ir))
        return ir

    elif bru>1500 and bru<=2500:
        ir = bru*0.10
        print('(-)Imposto de Renda: (10%)           : R${:7.2f} '.format(ir))
        return ir

    else:
        ir = bru*0.20
        print('(-)imposto de Renda: (20%)           : R${:7.2f} '.format(ir))
        return ir
    
def descontos(bru):

    sind = bru*0.03
    print('(-)Sindicato: (3%)       : R${:7.2f} '.format(sind))
    
    fgts = bru*0.11
    print('FGTS: (11%)           : R${:7.2f} '.format(fgts))
    return bru, sind

def total(ir, sind,bru):
    desc = ir+sind
    print('Total de descontos:           R${:7.2f}'.format(desc))

    liq = bru - desc 
    print('Salário Líquido:            R${:7.2f}'.format(liq))
    return desc, liq

#Main

ganho, cargoraria = ler()
salario_bruto = bruto(ganho, cargoraria)
imposto_renda = imposto(salario_bruto)
sindicato, imposto_fgts = descontos(salario_bruto)
total_descontos, salario_liquido = total(imposto_renda, sindicato,salario_bruto)



    

    
    
    
