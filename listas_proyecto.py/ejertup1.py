#Crear una tupla con las siguientes frutas 
#Manzana,Kiwi,Pera,Fresa,Uva,Pera
#Cuantas veces hay Pera
#saber si esque hay fresa 
#Si sandia no esta dar un mensaje de no hay 
frutas = ("Manzana","Kiwi","Pera","Fresa","Uva","Pera")
print("Las veces que aparece Pera son:", frutas.count("Pera"))
if "Fresa" in frutas:
    print("Si hay Fresa")
else:
    print("NO hay fresas")

if "Sandia" in frutas:
    print("HAY SANDIA")
else:
    print("NO HAY SANDIA")
    