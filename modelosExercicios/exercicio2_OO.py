

#1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro('Brasilia', 'Vermelho', 1975)


#2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.


class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao



