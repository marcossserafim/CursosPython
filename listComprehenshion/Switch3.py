def getTipoDia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    diaEscolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(diaEscolhido, '** dia inválido **')
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {getTipoDia(dia)}')
