class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praças'
restaurante_praca.categoria = 'Gourmet'
restaurante_pizza = Restaurante()


restaurante_praca.categoria = 'Italiana'
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

restaurantes = [ restaurante_praca, restaurante_pizza]

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
print(vars(restaurante_praca))