#Douglas


'''O programa deve ser modularizado e exibido com mensagens indicativas Ler uma uma quantidade indeterminada de nomes e idade.
Verificar se um nome lido se encontra neste grupo de dados.
Usar pesquisa binária.Pode usar sort().
Caso exista emitir a mensagem O nome xxxx com yy de idade foi encontrado.
Ou, O nome xxxx com yy de idade não foi encontrado.'''

def ler():
    lista = []
    while True:
        nome = input('Nome: ')
        if nome == '':
            break
        idade = input('Idade: ')
        lista.append(nome + ' ' + idade)
    lista.sort()
    separado = lista.split()
    
    return lista

def proc(lista):
    procurado = input('Pesquise um nome: ')
    inicio = 0
    fim = len(lista)-1
    achei = False
    meio = (inicio+fim)//2
        try:
            if lista[meio] == procurado and achei == False:
                achei = True
                
            elif lista[meio]<prucurado:
                lista[meio]+inicio
                print('{} foi encontrado'.format(procurado))
            else:
                lista[meio]-fim
                print('{} foi encontrado'.format(procurado))
        except:
            print('Não encontrado!')
    return

#Main
lista = ler()
proc(lista)
