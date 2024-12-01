#Exercícios
#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura\n')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
print(f'Meu nome é {nome} e tenho {idade} anos\n')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
array_alura = ['A', 'L', 'U', 'R', 'A']

#Com o uso de várias strings com o separador ‘sep’ indicando a quebra de linha entre cada uma delas, cada string será impressa com espaçamentos e quebras de linha.
print('A','L','U','R','A',sep='\n')


for letra in array_alura:
    print(letra)

#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e 
# arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159
pi_arredondado = round(pi, 2)

# Abordagem de f-string
print(f'\nO valor arredondado de pi é: {pi:.2f}\n')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}\n'.format(pi))

print(f'O valor arredondado de pi é: {pi_arredondado}\n')