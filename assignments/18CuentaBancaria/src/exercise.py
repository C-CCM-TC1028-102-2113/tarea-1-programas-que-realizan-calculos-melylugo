def main():
    #escribe tu código abajo de esta línea
    saldo=float(input("Dame el saldo del mes anterior: "))
    ingresos=float(input("Dame los ingresos: "))
    egresos=float(input("Dame los egresos: "))
    cheques=int(input("Dame el número de cheques: "))

    x=(saldo)+(ingresos)-((egresos)+(cheques*13))
    n=0.075*x
    saldoTotal= x-n
    saldoTotal=round(saldoTotal,5)
  
    print ("El saldo final de la cuenta es:",saldoTotal)
    pass

if __name__ == '__main__':
    main()
