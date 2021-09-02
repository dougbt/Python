'''faça um programa que recebe o salario de um colaborador e o reajuste segundo o seguinte criterio'''

def ler():
    sal_atual = float(input('Digite o seu salário: '))
    return sal_atual

def calc(sal_atual):
    if sal_atual<=280:
        aument = sal_atual*0.20
        sal_aument = sal_atual+aument
        print('O salário era R${}, com aumento de 20%(R${}) você passará a receber R${} '.format(sal_atual, aument, sal_aument))
        return aument, sal_aument
    
    elif sal_atual>280 and sal_atual<=700:
        aument = sal_atual*0.15
        sal_aument = sal_atual+aument
        print('O salário era R${}, com aumento de 15%(R${}) você passará a receber R${} '.format(sal_atual, aument, sal_aument)) 
        return aument, sal_aument
    
    elif sal_atual>700 and sal_atual<=1500:
        aument = sal_atual*0.10
        sal_aument = sal_atual+aument
        print('O salário era R${}, com aumento de 10%(R${}) você passará a receber R${} '.format(sal_atual, aument, sal_aument))
        return aument, sal_aument
    else:
        aument = sal_atual*0.05
        sal_aument = sal_atual+aument
        print('O salário era R${}, com aumento de 5%(R${}) você passará a receber R${} '.format(sal_atual, aument, sal_aument))  
        return aument, sal_aument

#Main

atual = ler()
aumento,novo = calc(atual)

