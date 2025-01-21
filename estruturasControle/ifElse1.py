#!/usr/local/bin/python3
def notaConceito(valor):
    nota = float(valor)
    
    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-' 
    else: 
        return 'Nota Invalida'

if __name__ == '__main__':
    valorInformado = input('Nota do aluno: ')
    conceito = notaConceito(valorInformado)
    print(conceito)
    
    
#     nota = sys.argv[0]
#     print('A sua nota é  !'



# if nota >= 9:
#       print('A')
# elif nota >= 8:
#     print('A-')
# elif nota >= 7:
#     print('B')
# elif nota >= 6:
#     print('C')
# elif nota >= 5:
#     print('C-')
# elif nota >= 4:
#     print('D')
# elif nota >= 3:
#     print('D-')
# elif nota >= 2:
#     print('E')
# elif nota >= 1:
#     print('E-')    
# else:
#     print('Nota Inválida')    

# 'A' = 10 or 9.1
# 'A-'= 9 or 8.1
# 'B' = 8 or 7.1
# 'B-'= 7 or 6.1
# 'C' = 6 or 5.1
# 'C-'= 5 or 4.1
# 'D' = 4 or 3.1
# 'D-'= 3 or 2.1
# 'E' = 2 or 1.1
# 'E-'= 1 or 0.1



#  *Para notas maiores que a nota 10 e menores que 0 sera impresso "Nota Inválidas"


            
