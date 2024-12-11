class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self) :
        print(f'{self.nome} | {self.artista} | {self.duracao}')

    def listar_musicas():
        for musisaRecebida in Musica.musicas:
            print(f'{musisaRecebida.nome} | {musisaRecebida.artista} | {musisaRecebida.duracao}')
        




musica_rock = Musica('Duallity', 'Slipknot', 300)

""" musica_rock.nome = 'Duallity'
musica_rock.artista = 'Slipknot'
musica_rock.duracao = 300 """


musica_samba = Musica('Cabide', 'Martinalia', 350)

""" musica_samba.nome = 'Cabide'
musica_samba.artista = 'Martinalia'
musica_samba.duracao = 350 """


musica_pagode = Musica('Sinais', 'Sorriso Maroto', 400)

""" musica_pagode.nome = 'Sinais'
musica_pagode.artista = 'Sorriso Maroto'
musica_pagode.duracao = 400 """




""" print(vars(musica_rock))
print(vars(musica_samba))
print(vars(musica_pagode)) """

Musica.listar_musicas()