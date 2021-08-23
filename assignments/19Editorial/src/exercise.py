def main():
    #escribe tu código abajo de esta línea
    import math

    palabras=int(input("Dame el número de palabras: "))

    x=(math.ceil(palabras/475))*60
    desc=x*0.10
    Total=x-desc
    Total=round(Total,1)

    print("El costo de la publicación es:",Total)
    pass

if __name__ == '__main__':
    main()
