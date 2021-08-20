def main():
    #escribe tu código abajo de esta línea
    import math

    palabras=int(input("Dame el numero de palabras: "))

    x=(math.ceil(palabras/475))*60
    desc=x*0.10
    Total=x-desc
    Total=round(Total,1)

    print(Total)
    pass

if __name__ == '__main__':
    main()
