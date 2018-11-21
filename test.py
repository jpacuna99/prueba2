# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("Adios mundo cruel")


x=np.linspace(-2.,2.,50)
plt.plot(x**2,x)
plt.savefig("hola")

