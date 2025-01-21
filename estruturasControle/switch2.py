# def getTipoSemana(dia):
#     dias = {
#         1: 'Fim de semana',
#         2: 'Dia da semana',
#         3: 'Dia da semana',
#         4: 'Dia da semana',
#         5: 'Dia da semana',
#         6: 'Dia da semana',
#         7: 'Fim de semana'
#     }
#     return dias.get(dia, '** inválido **')


# if __name__ == '__main__':
#     for dia in range(0, 9):
#         print(f'{dia}: {getTipoSemana(dia)}')

def get_tipo_dia(dia):
    match dia:
        case 2 | 3 | 4 | 5 | 6 :
            return 'Dia de semana'
        case 1 | 7:
            return 'Fim de semana'
        case _:
            return '** inválido **'
            
 
 
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')