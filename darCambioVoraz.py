def cambio(denominaciones, cantidad):
    mapa={}
    acumulado=0
    for i in denominaciones:
        while i+acumulado <= cantidad:
            acumulado+=i
            if not i in mapa:  
                mapa[i]=1
            else:
                mapa[i]=+1
    return mapa 
print(cambio([5,2,1],12))       
     
def dar_vueltas(denominaciones, cantidad):
  1     vueltas = {} 
  2     for i in reversed(denominaciones): 
  3         while cantidad - i > 0:
  4             if i in vueltas:
  5                 vueltas[i] += 1
  6             else:
  7                 vueltas[i] = 0
  8             cantidad -= i
  9     return vueltas