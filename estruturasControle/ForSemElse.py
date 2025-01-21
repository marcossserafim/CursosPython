PALAVRASPROIBIDAS = ('futebol', 'política', 'religião')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRASPROIBIDAS:
            print('Texto possiu pelo menos uma palavra proibida', palavra)
            found = True
            break
        
if not found:
    print('Texto autorizado', texto)