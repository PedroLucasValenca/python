

#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.


numero_informado = input('Digite um número: ')

tamanho_numero_informado = len(numero_informado)

digito_final_numero_informado = int(numero_informado[-1])


if digito_final_numero_informado == 0:
    print(f'Número {numero_informado} é impar!\n')
elif digito_final_numero_informado == 2:
    print(f'Número {numero_informado} é impar!\n')
elif digito_final_numero_informado == 4:
    print(f'Número {numero_informado} é impar!\n')
elif digito_final_numero_informado == 6:
    print(f'Número {numero_informado} é impar!\n')
elif digito_final_numero_informado == 8:
    print(f'Número {numero_informado} é impar!\n')
elif digito_final_numero_informado == 1:
    print(f'Número {numero_informado} é par!\n')
elif digito_final_numero_informado == 3:
    print(f'Número {numero_informado} é par!\n')
elif digito_final_numero_informado == 5:
    print(f'Número {numero_informado} é par!\n')
elif digito_final_numero_informado == 7:
    print(f'Número {numero_informado} é par!\n')
else:
    print(f'Número {numero_informado} é par!\n')


#EXERCICIO RESOLVIDO PELO PROFESSOR
#numero = int(input("Digite um número: "))
#if numero % 2 == 0:
#    print("O número é par.")
#else:
#    print("O número é ímpar.")



#match digito_final_numero_informado:
#    case 0:
#        print(f'Número {numero_informado} é impar!')
#    case 2:
#        print(f'Número {numero_informado} é impar!')
#    case 4:
#        print(f'Número {numero_informado} é impar!')
#    case 6:
#        print(f'Número {numero_informado} é impar!')
#    case 8:
#        print(f'Número {numero_informado} é impar!')
#    case 1:
#        print(f'Número {numero_informado} é par!')
#    case 3:
#        print(f'Número {numero_informado} é par!')
#    case 5:
#        print(f'Número {numero_informado} é par!')
#    case 7:
#        print(f'Número {numero_informado} é par!')
#    case 9:
#        print(f'Número {numero_informado} é par!')


#2 - Pergunte ao usuário sua idade e, com base nisso, 
# use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:


#EXERCICIO RESOLVIDO PELO PROFESSOR
#idade = int(input("Digite sua idade: "))
#if 0 < idade <= 12:
#    print("Criança")
#elif 12 < idade < 18:
#    print("Adolescente")
#elif idade >= 18:
#    print("Adulto")
#else: 
#    print("Valor inválido!")

idade_informada = int(input('Informe a idade do usúario: '))

if idade_informada >= 0 and idade_informada <= 12:
    print('Criança: 0 a 12 anos\n')
elif idade_informada >= 13 and idade_informada <= 18:
    print('Adolescente: 13 a 18 anos\n')
elif idade_informada > 18:
    print('Adulto: acima de 18 anos\n')
else:
    print('Valor inválido')



#3 - Solicite um nome de usuário e uma senha e 
# use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


nome_esperado = 'pedro'
senha_esperada = int(1234)


nome_informado = input('Informe o nome do usuário: ')
senha_informado = int(input('Informe a senha númerica: '))

if nome_esperado == nome_informado and senha_esperada == senha_informado:
    print('Valores informados estão corretos\n')
else:
    print('Valores informado são diferentes dos esperados!\n')





#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize 
# uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.


numero_x = float(input("Informe a coordenada de x: "))
numero_y = float(input("Informe a coordenada de y: "))


if numero_x > 0 and numero_y > 0:
    print('Primeiro Quadrante')
elif numero_x < 0 and numero_y > 0:
    print('Segundo Quadrante')
elif numero_x < 0 and numero_y < 0:
    print('Terceiro Quadrante')
elif numero_x > 0 and numero_y < 0:
    print('Quarto Quadrante')
else:
    print('o ponto está localizado no eixo ou origem')