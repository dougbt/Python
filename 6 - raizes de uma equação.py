'''faça um programa que calcule as raizes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e ce fazer as consistencias, informando ao usuarios as seguites situações:'''

def ler():
    a = float(input('Digite o valor de A: '))
    if a==0:
        print('com x=0 a equação não é de segunda grau')
    else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    return a,b,c

def calc(a,b,c):
    delta = b**2 - 4*a*c
    x1 = (-b+delta**(1/2))/2*a
    x2 = (-b-delta**(1/2))/2*a
    return delta, x1, x2

def imprim(delta,x1,x2):
    print('delta: {:4.2f}'.format(delta))
    print('x1: {:4.2f}'.format(x1))
    print('x2: {:4.2f}'.format(x2))
    return

a,b,c = ler()
delta1, y1, y2 = calc(a,b,c)
imprim(delta1,y1,y2)
