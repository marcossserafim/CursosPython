#  [ expressão for iten in list if condicional]
dobroDosPares = [i * 2 for i in range(10) if i % 2 == 0]

print(dobroDosPares)

#  Versão "normal"
dobrosDosPares = []
for i in range(10):
    if i % 2 == 0:
        dobrosDosPares.append (i * 2)
print(dobrosDosPares)
