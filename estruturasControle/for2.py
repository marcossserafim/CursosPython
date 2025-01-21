palavra = 'Paralelepipido'
for letra in palavra:
    print(letra, end=",")
print('Fim')
9
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
    
for posicao, nome in enumerate(aprovados):
    print(f'{posicao +1})', nome)
    
diasSemana = ('Domingo', 'Segunda', 'Terça',
              'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in diasSemana:
    print(f'Hoje é {dia}')
    
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
