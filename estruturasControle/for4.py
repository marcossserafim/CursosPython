# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')
from random import randint

def sortearDados():
    return randint(1, 6)



for i in range(1, 7):
    if i % 2 == 1:
       continue
      
    if sortearDados() == i:
        print('Acertou!', i )
        break
else:
    print('Não Acertou o número')          





 