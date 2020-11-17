# Practica3.py-P3E6
#Pida al usuario el precio de un producto y el nombre del producto y muestre el
#mensaje con el precio del IVA (21%). Por ejemplo: �Tu bicicleta vale 100 euros 
#y con el 21 % de IVA se queda en 121 euros en total�.
price=float(input("Introduzca el precio de un producto "))
name=input("Introduzca el nombre del producto ")
iva=price+(price*0.21)
print("Su", name, "vale", price,"euros y con el 21% de IVA se queda en", iva, "euros en total")
