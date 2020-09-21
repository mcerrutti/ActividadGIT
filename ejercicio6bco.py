cap = 0
tasa = 0.02
tiempo = 0
Capret = 0
tasado = 0
print ("Vamos a calculcar cuanto cobrariamos en x tiempo al invertir el capital")
cap= int(input("Ingresa el valor de tu capital: "))
tiempo = int(input("En cuantos meses deseas calcularlo: "))
tasado = ( cap * tasa * tiempo)
capret = cap + tasado
print (" EL DINERO AL CABO DE : ",tiempo,"meses" " Usted recibira: ",capret, "El % de la tasa es del: ",tasa)
