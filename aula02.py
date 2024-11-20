

#verificar se as idades são maiores, menores ou iguais

'''usuario1 = int(input('qual sua idade?   '))
usuario2 = int(input('qual sua segunda idade?   '))

if ( usuario1 > usuario2):
    print ('a idade do usuario 1 é maior que usuario2')
elif ( usuario2 > usuario1):
    print ('a idade do usuario 2 é maior que usuario1')

else:
    print ('as idades são iguais')'''

# verificar se os nomes são iguais ou diferentes

'''nome1 = input (' qual seu nome?  ').lower() .strip()

nome2 = input (' qual seu nome?  ').lower() .strip()

if (nome1 == nome2):
    print ('seus nomes são iguais')
else:
    print (' seus nomes são diferentes')'''

# verificar se o individuo pode dirigir ou não
'''idade = int (input('qual sua idade?  '))
habilitacao = input(' você possui habilitação (sim ou não)')

if (idade >= 18 and habilitacao == 'sim' ):
    print ( ' você pode dirigir')
else:
    print (' você não pode dirigir')'''

# verifica se o aluno passou ou não na média

'''bimestre1 = int (input(' qual sua nota no primeiro trimestre? '))
bimestre2 = int (input(' qual sua nota no segundo trimestre? '))
bimestre3 = int (input(' qual sua nota no terceiro trimestre? '))
bimestre4 = int (input(' qual sua nota no quarto trimestre? '))

nota = (bimestre1 + bimestre2 + bimestre3 + bimestre4) /4

if ( nota >= 6 ):
    print (f' aluno aprovado, sua nota foi {nota}')
else:
    print (f'aluno reprovado, sua nota foi {nota}')'''

# desconto de 5% no produto

'''produto = 100
desconto = 5/100

produto -= produto * desconto

print (f'seu desconto foi {produto:.2f}')'''

# dobro do valor de um produto

'''produtoBlackfraude = 100
produtoBlackfraude *= 2

print(f' produto está com desconto de: {produtoBlackfraude:.2f}')'''

# verificar se o caractere está na frase ou não

'''frase = input ('digite uma frase')
caractere = input (' digite uma palavra')

if ( caractere in frase):

    print(f' o caracter {caractere} está na frase')

else:
    print(f' o caracter {caractere}  não está na frase')'''

# verificar se uma palavra está em uma frase

'''frase = input ('digite uma frase')
palavra = input (' digite uma palavra')

if ( palavra in frase):

    print(f' a palavra {palavra} está na frase')

else:
    print(f' a palavra {palavra} não está na frase')'''