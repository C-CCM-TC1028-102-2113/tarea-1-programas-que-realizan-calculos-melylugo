def main():
    #escribe tu código abajo de esta línea
    
    # Elia Melissa Lugo Vences
    # A01660980
    # Programa que calcula la distancia recorrida por un caracol"
    
    minutos=float(input("Dame los minutos: "))

    unidades=5.7*(1/10)*(60/1)
    distancia=minutos*unidades
    distancia=round(distancia,1)
    print ("Centímentros recorridos: ", distancia)

if __name__ == '__main__':
    main()
