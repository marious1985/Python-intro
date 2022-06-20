def numero_primo():
    numero: int = int(input('Introduce un entero:'))

    if numero > 1:
        #Buscamos los factores del numero
        for i in range(2,int(numero)):
            if (int(numero) % i) == 0:
                print ("La jodiste, el numero", numero, "NO ES PRIMO. Es divisible entre", i)
                break
            else:
                print ("Eres un crack, el numero", numero, "ES PRIMO")
                break
    else:
        print("Lo siento, el numero", numero, "NO ES PRIMO. Los numeros primos son mayores que 1")

numero_primo()
