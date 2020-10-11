def maximo(arreglo):
    if len(arreglo)==1:
        return arreglo[0]
    pivote = len(arreglo)//2
    mI = maximo(arreglo[0:pivote])
    mD= maximo(arreglo[pivote:])
    return mI if mI>mD else mD
    

print(maximo([104,6,9,1,5,6,8,105]))

