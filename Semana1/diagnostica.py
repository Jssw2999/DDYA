import math

#1
def signo(n):
    if n < 0:
        resp = "negativo"
        return resp
    elif n > 0:
        resp = "positivo"
        return resp
    else:
        resp = "El numero es 0"
        
#2
def par_imp(n):
    if n%2 == 0:
        resp = "par"
        return resp
    else:
        resp = "impar"
        return resp

#3
def fibonacci(n):
    secu = []
    i = 0
    terminado = False
    while terminado != True:
        if len(secu) <= 1:
                secu.append(1)
                i += 1
        else:
            while secu[i-1] < n:
                
                secu.append(secu[i-2] + secu[i-1])
                i += 1
            if secu[i-1] == n:
                print("esta en fibonacci")
            terminado = True   
        

#4
def primo(n):
    if n <= 1:
        return "No es primo"  
    
    for i in range(2, n):
        if n % i == 0:
            return "No es primo"  
            
    return "Es primo"


#5
def sum_inter(n1, n2):
    inter1 = n1/2
    inter2 = n2/2

    return inter1 + inter2
    
    
#6
def parimp_pot(n):
    if n%2 == 0:
        resp = n ** 2
        return resp
    else:
        resp = n ** 3
        return resp

#7

def main():
    data = input("Ingrese los dígitos: ")
    digitos_validos = ["1","2","3","4","5","6","7","8","9","0"]
    nums = []
    dia = []
    codigo = []
    if len(data) == 19:
        for caracter in data:
            if caracter in digitos_validos:
                nums.append(caracter)
        print(nums)
        dia.append(nums[0])
    elif len(data) == 20:
        for caracter in data:
            if caracter in digitos_validos:
                nums.append(caracter)
        print(nums)
        for i in range(2):
            dia.append(nums[i])
    else:
        print("Revise que su entrada tenga 19 o 20 digitos")
    print(dia)
        

main()


    
