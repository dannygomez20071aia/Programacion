import timeit
#el uso de "variable":. 1f = es para utilizar la cantidad de decimales q se desea 

lista = [1,2,3,4,5,6]
tup = (1,2,3)
tiempo = timeit.timeit(stmt="list[2]",setup="lista = [1,2,3]",number=1000000)
tie = timeit.timeit(stmt="tup[2]",setup="tup = (1,2,3)",number=1000000)

print(f"La velocidad de respeusta de LISTA es es :{tiempo:.6f}")
print(f"La velocidad de respeusta de TUPLA es :{tie:.6f}")


