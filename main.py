import pickle

from Vehiculo import Vehiculo

f = open("C:/Users/minch/OneDrive/Escritorio/datos.dat", 'wb')
coche = Vehiculo("Mercedes","Rojo", 5)

pickle.dump(coche, f)
f.close()

w = open("C:/Users/minch/OneDrive/Escritorio/datos.dat", 'rb')
auto = pickle.load(w)
w.close()

print(auto.marca)

