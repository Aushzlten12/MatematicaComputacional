import numpy as np
# Operaciones con Matrices que se necesitan para el Metodo Simplex
def OperacionFila(Matriz,f1,f2,k=1):
    n = Matriz[0].__len__()
    for i in range(n):
        Matriz[f1][i] += k*Matriz[f2][i]

def MayorAbsoluto(Array):
    n = Array.__len__()
    Fila = np.zeros(n-1)
    for i in range(n-1):
        Fila[i] = Array[i]
    FilaAbs = list(map(lambda x:abs(x),Fila))
    maxVal = max(FilaAbs)
    # Encontrar el indice 
    ind = 0
    for i in range(Fila.__len__()):
        if abs(Fila[i]) == maxVal:
            ind = i
            break
    return maxVal,ind

def EncontrarMenorEnFila(Matriz,ColMultiply,NumeroVariables):
    indiceColumna = 0
    n = Matriz[0].__len__()
    ArraySumasDeConstante = np.zeros(n-1)
    ArraySumasNoConstante = np.zeros(n-1)
    for i in range(n-1):
        sumaConst = 0
        sumaNoConst = 0
        for j in range(ColMultiply.__len__()):
            if ColMultiply[j] == 0:
                sumaConst += Matriz[j][i]
            else:
                sumaNoConst += ColMultiply[j]*Matriz[j][i]
            
        ArraySumasDeConstante[i] = -1 *sumaConst
        ArraySumasNoConstante[i] = -1 * sumaNoConst
        if (i - NumeroVariables) % 2 == 1 and i-NumeroVariables>=0:
            ArraySumasDeConstante[i] += 1
        else:
            ArraySumasNoConstante[i] += Matriz[Matriz.__len__()-1][i]
    MinVal = min(ArraySumasDeConstante)
    indiceColumna = IndiceEnArray(MinVal,ArraySumasDeConstante)
    if VecesApareceEnArray(ArraySumasDeConstante,MinVal)>1:
        indices = IndicesConValorEnArray(ArraySumasDeConstante,MinVal)
        MinVal = ArraySumasNoConstante[indices[0]]
        for ind in indices:
            if ArraySumasNoConstante[ind]<MinVal:
                MinVal = ArraySumasNoConstante[ind]
        indiceColumna = IndiceEnArray(MinVal,ArraySumasNoConstante)
    condicion = False
    if FilaNoNegativa(ArraySumasDeConstante) and FilaNoNegativa(ArraySumasDeConstante):
        condicion = True
    return indiceColumna,condicion

def IndiceEnArray(n,Array):
    indice = 0
    for i in range(Array.__len__()):
        if n == Array[i]:
            return indice
        indice+=1
    return indice

def IndicesConValorEnArray(Array,n):
    indices = []
    for i in range(Array.__len__()):
        if n==Array[i]:
            indices.append(i)
    return indices
def VecesApareceEnArray(Array,n):
    Nveces = 0
    for i in range(Array.__len__()):
        if(n==Array[i]):
            Nveces +=1
    return Nveces

def FilaPorConstante(Matriz,f,k):
    for i in range(Matriz[0].__len__()):
        Matriz[f][i] *= k

def ConstruirTablaMaximizar(MatrizA,MatrizB,MatrizZ):
    n = MatrizA.__len__()
    m = 1
    p = MatrizZ.__len__()
    Tabla = np.zeros((n+1,1+m+p+n))
    for i in range(n):
        Tabla[i][0] = 0
        ind = 1
        for j in range(p):
            Tabla[i][ind] = MatrizA[i][j]
            ind+=1
        for j in range(n):
            if i==j:
                Tabla[i][ind]=1
            else:
                Tabla[i][ind]=0
            ind+=1
        Tabla[i][ind] = MatrizB[i][0]
    Tabla[n][0] = 1
    for i in range(1,1+m+p+n):
        if i <= MatrizZ.__len__():
            Tabla[n][i] = -1 * MatrizZ[i-1]
        else:
            Tabla[n][i] = 0
        
    return Tabla

def ConstruirTablaMinimizar(MatrizA,MatrizB,MatrizZ):
    n = MatrizA.__len__() # Numero de Ecuaciones de Restriccion
    m = 1 # Una columna de B
    p = MatrizZ.__len__() # Numero de Variables
    Tabla = np.zeros((n+1,p+m+2*n))
    for i in range(n):
        ind = 0
        for j in range(p):
            Tabla[i][ind] = MatrizA[i][j]
            ind+=1
        for j in range(n*2):
            if j==2*i:
                Tabla[i][ind] = -1
            elif j==2*i+1:
                Tabla[i][ind] = 1
            else:
                Tabla[i][ind] = 0
            ind+=1
        Tabla[i][ind] = MatrizB[i][0]
    for i in range(p+m+2*n):
        if i<p:
            Tabla[n][i] = MatrizZ[i]
        else:
            if (i-p)%2==0 and i-p>=0:
                Tabla[n][i] = 0
            else:
                Tabla[n][i] = 1
    return Tabla

def EncontrarPivote(Tabla,indiceColumna):
    n = Tabla.__len__()
    m = Tabla[0].__len__()
    ColumnaDivision = np.zeros(n-1)
    for i in range(n-1):
        if Tabla[i][indiceColumna]==0:
            ColumnaDivision[i] = -1
        else:
            ColumnaDivision[i] = Tabla[i][m-1] / Tabla[i][indiceColumna]
    minimaDivision = max(ColumnaDivision)
    for i in range(n-1):
        if ColumnaDivision[i]<0:
            continue
        if ColumnaDivision[i]<minimaDivision:
            minimaDivision = ColumnaDivision[i]
    indiceFila = 0
    for i in range(n-1):
        if ColumnaDivision[i] == minimaDivision:
            indiceFila = i
    pivote = Tabla[indiceFila][indiceColumna]
    return pivote,indiceFila

def FilaNoNegativa(Array):
    condicion = True
    for i in range(Array.__len__()):
        if Array[i]<0:
            condicion = False
            return condicion
    return condicion

def ColumnasDelPivoteCero(Matriz,indFila,indCol):
    n = Matriz.__len__()
    for i in range(n):
        if i == indFila:
            continue
        k = Matriz[i][indCol] / Matriz[indFila][indCol]
        OperacionFila(Matriz,i,indFila,-k)
def ColumnaDelPivoteCero(Matriz,indFila,indCol):
    n = Matriz.__len__()
    for i in range(n-1):
        if i == indFila:
            continue
        k = Matriz[i][indCol] / Matriz[indFila][indCol]
        OperacionFila(Matriz,i,indFila,-k)
def ArrayConCeros(Array):
    for i in range(Array.__len__()):
        if Array[i]==0:
            return True
    return False
def ProbarOptimoValor(Solucion,z,SolMaxima):
    VariablesColumna = np.zeros((z.__len__()))
    for i in range(z.__len__()):
        VariablesColumna[i] = Solucion[i][0]
    ValMax = 0
    for i in range(Solucion.__len__()):
        ind = int(Solucion[i][0])-1
        ValMax += Solucion[i][1] * z[ind] 
        if VariablesColumna[i] != 0:
            indice = int(Solucion[i][0])
            print(f"La variable x{indice} es igual a",round(Solucion[i][1],1))
    if ArrayConCeros(VariablesColumna):
        print("Las otras variables son iguales a 0")
    if ValMax == SolMaxima:
        print("La solucion maxima es : " ,round(SolMaxima,1))
    else:
        print("No se encontra la solucion maxima")

def ConseguirValorMinimo(Solucion,z):
    VariablesColumna = np.zeros((z.__len__()))
    for i in range(z.__len__()):
        VariablesColumna[i] = Solucion[i][0]
    MinimoValor = 0
    for i in range(z.__len__()):
        indice = int(Solucion[i][0])-1
        if indice >= 0:
            MinimoValor += Solucion[i][1] * z[indice]
            print(f"El valor de x{indice+1} es: ",round(Solucion[i][1],1))
    if ArrayConCeros(VariablesColumna):
        print("Las otras variables son iguales a 0")
    return MinimoValor
