class Restaurante:

    restaurantes = []
    '''construtor em python'''
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    '''metodo para retornar como desejo apresentar objeto'''
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    '''metodo criado dentro da propria classe'''
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

'''aula 1 exercicio'''
""" restaurante_praca.categoria = 'Italiana'
nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

categoria = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'


restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')


restaurante_pizza.ativo = True

restaurantes = [ restaurante_praca, restaurante_pizza] """

Restaurante.listar_restaurante()