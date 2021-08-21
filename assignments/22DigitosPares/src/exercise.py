def main():
    #escribe tu código abajo de esta línea
    
    digito=int(input("Dame un número: "))
    
    dPar=0
    
    if digito>-10000 and digito<=-1000 or digito>=1000 and digito<10000:
        while (digito>0):
            if digito%2==0:
                dPar=dPar+1
            else: 
                dPar=dPar+0
            digito=digito//10
        print("El número de dígitos pares es:",dPar)
    else: 
        print ("No cumple con las condiciones.")
        
    pass

if __name__ == '__main__':
    main()
