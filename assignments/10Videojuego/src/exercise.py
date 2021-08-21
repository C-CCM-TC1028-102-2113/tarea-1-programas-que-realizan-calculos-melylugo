def main():
    #escribe tu código abajo de esta línea
    
    new=int(input("Dame la cantidad de juegos nuevos: "))
    old=int(input("Dame la cantidad de juegos usados: "))
    
    total=int((new*1000)+(old*350))
    
    print ("El total de la compra es:",total)
    pass

if __name__ == '__main__':
    main()
