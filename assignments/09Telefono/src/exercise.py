def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    # Elia Melissa Lugo Vences
    # A01660980
    # Costo del teléfono

    print ("Dame el número de mensajes: ")
    msj=int(input())
    print ("Dame el número de megas: ")
    megas=float(input())
    print ("Dame el número de minutos ")
    minutos=int(input())

    costo = (msj*0.80) + (megas*0.80) + (minutos*0.80)

    print ("El costo mensual es: ")
    print (costo)

    pass


if __name__ == '__main__':
    main()
