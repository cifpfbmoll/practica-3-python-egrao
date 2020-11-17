# Practica3.py-P3E7 Pida al usuario tres n�mero que ser�n el d�a, mes y a�o. Comprueba que la fecha introducida es v�lida.  Por ejemplo: 
#32/01/2017->Fecha incorrecta
#29/02/2017->Fecha incorrecta
#30/09/2017->Fecha correcta.
day=int(input("Introduzca un dia"))
month=int(input("Introduzca el mes"))
year=int(input("Introduzca un year"))
if (day==31 and month==4 or month==6 or month==9 or month==11):
    print("Fecha invalida")
elif(day<=29 and (month==2)):
    print("Fecha invalida")
elif(month>12):
    print("Fecha invalida")
