from cola import Cola
from random import randint

cola = Cola()

# #! carga
for i in range(10):
    value = chr(randint(65, 90))
    print(value)
    cola.arrive(value)

#!  d, f, e, g, j, i, a
print()
cont = 0
total = cola.size()
while cont < total:
    if cola.on_front() in ['A', 'E', 'I', 'O', 'U']:
        cola.atention()
    else:
        cola.move_to_end()
    cont += 1

cont = 0
while cont < cola.size():
    value = cola.move_to_end()
    print(value)
    cont += 1