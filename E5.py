# Practica3.py-P3E5 Pida un n�mero que como m�ximo tenga tres cifras (por ejemplo ser�an v�lidos 1, 99 i 213 pero no 1001). 
#Si el usuario introduce un n�mero de m�s de tres cifras debe un informar con un mensaje de error como este �ERROR: El n�mero 1005 
#tiene m�s de tres cifras�.
num=int(input("Introduzca un numero con un maximo de 3 cifras "))
if (num>999):
    print("ERROR El numero", num,"tiene mas de tres cifras")
