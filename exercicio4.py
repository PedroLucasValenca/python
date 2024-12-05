

#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

nome_usuario = {'nome': 'Pedro', 'idade': 33, 'cidade': 'Curitiba'}
print(f'{nome_usuario} \n')

#2 - Utilizando o dicionário criado no item 1:


#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
nome_usuario['idade'] = 55
print(f'{nome_usuario} \n')

#Adicione um campo de profissão para essa pessoa;
nome_usuario['profissao'] = 'desenvolvedor'
print(f'{nome_usuario} \n')

#Remova um item do dicionário.
del nome_usuario['cidade']
print(f'{nome_usuario} \n')

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

#não funcionou corrigir
lista_numeros = [ {'numero':1}, {'numero':2}, {'numero':3}, {'numero':4}, {'numero':5}]

for numero in lista_numeros:
    quadrado_numero = numero[numero] * numero[numero]
    numero['quadrado'] = quadrado_numero

print(lista_numeros)   

#resolução instrutor
#numeros_quadrados = {x: x**2 for x in range(1, 6)}
#print(numeros_quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

#resolução instrutor
#pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
#if 'nome' in pessoa:
#    print("A chave 'nome' existe no dicionário.")
#else:
#    print("A chave 'nome' não existe no dicionário.")


#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.


#frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
#contagem_palavras = {}
#palavras = frase.split()
#for palavra in palavras:
#    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
#print(contagem_palavras)