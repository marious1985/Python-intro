
def anio_bisiesto ():
    anio =  int(input("Escribe un anio"))
    if (anio % 4 == 0) and (anio % 100 == 0) and (anio % 400 ==0):
        print(anio, "es un anio bisiesto")
    elif (anio % 4 == 0) and (anio % 100 != 0):
        print(anio, "es un anio bisioeso")
    else:
        print(anio, "no es anio bisioesto")

anio_bisiesto()
