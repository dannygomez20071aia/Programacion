#genera TUPLA ()
#Genera LISTA []


tup = [1,2,3]
tup[0] = 10
print(tup)



tup = (1,2,3)
print(tup)

import sys
x = [7,8,9]
y = (7,8,9)
print(f"Peso del formato de LISTA:{sys.getsizeof(x)}bytes")
print(f"Peso del formato de TUPLA:{sys.getsizeof(y)}Bytes")
