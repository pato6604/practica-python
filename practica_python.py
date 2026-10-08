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
    
    
    
    
    
    

print(ordenados([1,3,3,22]))