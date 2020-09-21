#DECLARACION DE VARIABLES#
cap = 0 #CAPITAL INICIAL#
tasa = 0.02 #LA TASA DE INTERESE#
tiempo = 0 #TIEMPO QUE DURA EL PLAZO FIJO#
Capret = 0 #DINERO QUE SE RETIRA AL FINALIZAR EL PLAZO FIJO#
tasado = 0 #EL MONTO DEL INTERES#

#ZONA RESERVADA PARA INGRESOS DE DATOS#
print ("Vamos a calculcar cuanto cobrariamos en x tiempo al invertir el capital")
cap= int(input("Ingresa el valor de tu capital: "))
tiempo = int(input("En cuantos meses deseas calcularlo: "))

#ZONA RESERVDA PARA LOS CALCULOS#
tasado = ( cap * tasa * tiempo)
capret = cap + tasado

#ZONA RESERVADA PARA LA SALUDA DE DATOS Y MUESTRAS POR PANTALLAS#
print (" EL DINERO AL CABO DE : ",tiempo,"meses" " Usted recibira: ",capret, "El % de la tasa es del: ",tasa)
