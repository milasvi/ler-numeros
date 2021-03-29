
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

r = ''
while True:
    n = int(input('Digite um número de 0 a 10'))
    while n not in range(0, 11):
        n = int(input('Tente novamente. Digite um numero de 0 a 10'))
    print(f'{n} por extenso é {cont[n]}.')
    r = str(input('Deseja continuar?')).upper()[0]
    if r == 'N':
        print('Reclama da vida mas não vive sem ela. Enfim a hipocrisia...')
        print('Fim do programa, volte sempre.')

        break