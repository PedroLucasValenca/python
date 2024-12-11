class Musica:
    nome = ''
    artista = ''
    duracao = float



musica_rock = Musica()

musica_rock.nome = 'Duallity'
musica_rock.artista = 'Slipknot'
musica_rock.duracao = 300


musica_samba = Musica()

musica_samba.nome = 'Cabide'
musica_samba.artista = 'Martinalia'
musica_samba.duracao = 3.50


musica_pagode = Musica()

musica_pagode.nome = 'Sinais'
musica_pagode.artista = 'Sorriso Maroto'
musica_pagode.duracao = 400




print(vars(musica_rock))
print(vars(musica_samba))
print(vars(musica_pagode))