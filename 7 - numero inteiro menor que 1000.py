def ler():
    num = int(input('Digite um número inteiro: '))
    return num

def calc(num):
#achando a unidade
    unidade = num%10

#tirando a unidade da dezena
    num = num-unidade

#achando a dezena
    dezena = num%10

#achando a centena
    centena = (num-dezena)/10

#transformando em inteiros
    dezena=int(dezena)
    centena=int(centena)
    return unidade, dezena, centena

def imprim(unidade, dezena, centena):
    print('{} = {} centenas, {} dezenas e {} unidades '.format(unidade, dezena, centena))
    return 

num = ler()
unidade, dezena, centena = calc(num)
imprim(unidade, dezena, centena)

