PALAVRASPROIBIDAS = ('futebol', 'política', 'religião')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRASPROIBIDAS:
            print('Texto possiu pelo menos uma palavra proibida', palavra)
            break
        
    else:
        print('Texto autorizado', texto)