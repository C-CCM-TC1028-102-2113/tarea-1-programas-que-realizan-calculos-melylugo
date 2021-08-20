def main():
    #escribe tu código abajo de esta línea
    msj=int(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    minutos=int(input("Dame el número de minutos "))
    
    costo = (msj*0.80) + (megas*0.80) + (minutos*0.80)
    costo=round(costo,2)
    
    print ("El costo mensual es: ", costo)
    pass

if __name__ == '__main__':
    main()
