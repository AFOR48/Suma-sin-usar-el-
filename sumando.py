#Sirve para sumar dos números de una cifra, retonar valores en una lista de dos valores
def sumar_digitos(num1,num2):
    b = "0"
    if num1 == "0":
        a = num2
    elif num2 == "0":
        a = num1
    else:
        conjunto = {num1,num2}
        if conjunto == {"1"}:
            a = "2"
        elif conjunto == {"2"}:
            a = "4"
        elif conjunto == {"3"}:
            a = "6"
        elif conjunto == {"4"}:
            a = "8"
        elif conjunto == {"5"}:
            a = "0"
            b = "1"
        elif conjunto == {"6"}:
            a = "2"
            b = "1"
        elif conjunto == {"7"}:
            a = "4"
            b = "1"
        elif conjunto == {"8"}:
            a = "6"
            b = "1"
        elif conjunto == {"9"}:
            a = "8"
            b = "1"
        elif conjunto == {"1", "2"}:
            a = "3"
        elif conjunto == {"1", "3"}:
            a = "4"
        elif conjunto == {"1", "4"}:
            a = "5"
        elif conjunto == {"1", "5"}:
            a = "6"
        elif conjunto == {"1", "6"}:
            a = "7"
        elif conjunto == {"1", "7"}:
            a = "8"
        elif conjunto == {"1", "8"}:
            a = "9"
        elif conjunto == {"1", "9"}:
            a = "0"
            b = "1"
        elif conjunto == {"2", "3"}:
            a = "5"
        elif conjunto == {"2", "4"}:
            a = "6"
        elif conjunto == {"2", "5"}:
            a = "7"
        elif conjunto == {"2", "6"}:
            a = "8"
        elif conjunto == {"2", "7"}:
            a = "9"
        elif conjunto == {"2", "8"}:
            a = "0"
            b = "1"
        elif conjunto == {"2", "9"}:
            a = "1"
            b = "1"
        elif conjunto == {"3", "4"}:
            a = "7"
        elif conjunto == {"3", "5"}:
            a = "8"
        elif conjunto == {"3", "6"}:
            a = "9"
        elif conjunto == {"3", "7"}:
            a = "0"
            b= "1"
        elif conjunto == {"3", "8"}:
            a = "1"
            b = "1"
        elif conjunto == {"3", "9"}:
            a = "2"
            b = "1"
        elif conjunto == {"4", "5"}:
            a = "9"
        elif conjunto == {"4", "6"}:
            a = "0"
            b= "1"
        elif conjunto == {"4", "7"}:
            a = "1"
            b= "1"
        elif conjunto == {"4", "8"}:
            a = "2"
            b = "1"
        elif conjunto == {"4", "9"}:
            a = "3"
            b = "1"
        elif conjunto == {"5", "6"}:
            a = "1"
            b= "1"
        elif conjunto == {"5", "7"}:
            a = "2"
            b= "1"
        elif conjunto == {"5", "8"}:
            a = "3"
            b = "1"
        elif conjunto == {"5", "9"}:
            a = "4"
            b = "1"
        elif conjunto == {"6", "7"}:
            a = "3"
            b= "1"
        elif conjunto == {"6", "8"}:
            a = "4"
            b = "1"
        elif conjunto == {"6", "9"}:
            a = "5"
            b = "1"
        elif conjunto == {"7", "8"}:
            a = "5"
            b = "1"
        elif conjunto == {"7", "9"}:
            a = "6"
            b = "1"
        elif conjunto == {"8", "9"}:
            a = "7"
            b = "1"
        else:
            print("Algun número mal ingresado.")
            b = ""
            a = ""
        
        
    return [b,a]

#Puede sumar 3 números útil para hacer la pequeñas unidades y unidades decenas-decenas, centenas-centenas etc
def mini_suma(llevas,a,b):
    primera_suma = sumar_digitos(llevas,a)
    #print(primera_suma)
    segunda_suma = sumar_digitos(b,primera_suma[1])
    #print(segunda_suma)
    tercera_suma = sumar_digitos(primera_suma[0],segunda_suma[0])
    #print(tercera_suma)
    resultado = [tercera_suma[1],segunda_suma[1]]
    return resultado
    




numeros = ["0","1","2","3","4","5","6","7","8","9"]

def verificar_numeros(sumando):
    for caracter in sumando:
        if caracter in numeros:
            pass
        else:
            return False
            print(f"No es un número ({sumando})")
            break
    return True

def sumaFinal(sumando1,sumando2):
    #Iguala el número de digitos
    numero_digitos = max(len(sumando1),len(sumando2))
    if len(sumando2)>len(sumando1):
        sumando1="0"*(len(sumando2)-len(sumando1))+sumando1
    elif  len(sumando1)>len(sumando2):
        sumando2="0"*(len(sumando1)-len(sumando2))+sumando2
    else:
        pass
    
    #Se realiza la suma recorriendo los números como string    
    resultado = []
    llevas = "0"
    i = 1
    for i  in range(1,numero_digitos+1):
        digito = mini_suma(llevas,sumando1[-i],sumando2[-i])
        llevas = digito[-2]
        resultado.insert(0,digito[-1])
    if digito[0] != "0":
        resultado.insert(0,digito[0])
    return resultado

i=""
while i != "n":
    sumando1 = input("Ingresa el primer número: ")
    sumando2 = input("Ingresa el segundo número: ")
    if verificar_numeros(sumando1) and verificar_numeros(sumando2):
        resultado = sumaFinal(sumando1,sumando2)
        #print(resultado)
        resultado_texto = ""
        for caracter in resultado:
            resultado_texto = resultado_texto + caracter
        print(f"El resultado es {resultado_texto}")
    
    else:
        print("No se ingresaron los números correctamente")
    i = input("Si no deseas hacer otra suma escribe una n: ")

