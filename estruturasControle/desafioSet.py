PALAVRASPROIBIDAS = {'futebol', 'política', 'religião'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRASPROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavra proibida:', intersecao)
    else:
        print('Texto autorizado:', texto)