def pertenece(s: list[int], e: int) -> bool:
    res: bool = True
    for numero in s:
        if e == numero:
            return res 
    return False     



#print(pertenece([1,2,3],1))




def divide_todos(s:list[int], e:int) -> bool:
    res: bool = True
    for num in s:
        if num % e != 0:
            res = False
    return res 

#print(divide_todos([15,41,45], 5))




def suma_total(s:list[int]) -> int:
    res: int = 0
    for numero in s:
        res += numero 
        
    return res 



#print(suma_total([1,2,-3,4]))




def maximo(s:list[int]) -> int:
    max_actual: int = s[0]
    for numero in s:
        if numero > max_actual:
            max_actual = numero
        else:
            max_actual = max_actual
            
    return max_actual


#print(maximo([15000,-22,-3,2000]))




def minimo(s:list[int]) -> int:
    min_actual: int = s[0]
    for numero in s:
        if min_actual > numero:
            min_actual = numero
            
        else:
            min_actual = min_actual
            
    return min_actual



#print(minimo([-1,-22,-554]))




def ordenados(s:list[int]) -> bool:
    res: bool = True
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            res = False
            
    return res    
    
    
    
    
    
    

#print(ordenados([1,3,3,22]))



def pos_maximo(s:list[int]) -> int:
    max_actual: int = s[0]
    pos_maximo_actual: int = 0 
    
    
    for i in range(len(s)-1):
        if max_actual < s[i+1]:
            max_actual = s[i+1]
            pos_maximo_actual = i + 1
            
        
    return pos_maximo_actual




#print(pos_maximo([22,13333,300]))



def pos_minimo(s:list[int]) -> int:
    min_actual: int = s[0]
    pos_min_actual: int = 0
    
    
    for i in range(len(s)-1):
        if min_actual > s[i+1]:
            min_actual = s[i+1]
            pos_min_actual = i + 1
            
    return pos_min_actual




#print(pos_minimo([120,340,45,5]))        





def long_mayor_a_siete(s:str) -> bool:
    res: bool = False
    cantidad: int = 0 
    
    for letra in s:
        cantidad += 1
        
        if cantidad > 7:
            res = True
            
    return res 



#print(long_mayor_a_siete("Termo"))
            
    
    
    

def long_mayor_ASiete(s:list[str]) -> bool:
    res: bool = False
    
    for palabra in s:
        if long_mayor_a_siete(palabra):
            res = True
            
            
    return res 


#print(long_mayor_ASiete(["termo", "gato", "tener", "jirafas"]))



def iguales_consecutivos(s:list[int]) -> bool:
    res: bool = True
    
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            res = False
            
    return res 



print(iguales_consecutivos([1,1,3,4]))

