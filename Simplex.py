from Matrices import *

# Metodo Simplex para maximizar
def SimplexMaximizar(Tabla,Solucion):
    n = Tabla.__len__()
    m = Tabla[0].__len__()
    while not FilaNoNegativa(Tabla[n-1]):
        indCol = MayorAbsoluto(Tabla[n-1])[1]
        pivote, indFila = EncontrarPivote(Tabla,indCol)
        FilaPorConstante(Tabla,indFila,1/pivote) 
        ColumnasDelPivoteCero(Tabla,indFila,indCol)
        Solucion[indFila][0] = indCol 
    for i in range(Solucion.__len__()):
        if Solucion[i][0]!=0:
            Solucion[i][1] = Tabla[i][m-1]
    return Tabla[n-1][m-1]

# Metodo Simplex para minimizar
def SimplexMinimizar(Tabla,Solucion,NumeroVariables):
    n = Tabla.__len__()
    m = Tabla[0].__len__()
    ColMultiply = np.zeros(n-1)
    while not EncontrarMenorEnFila(Tabla,ColMultiply,NumeroVariables)[1]:
        indCol= EncontrarMenorEnFila(Tabla,ColMultiply,NumeroVariables)[0]
        pivote,indFila = EncontrarPivote(Tabla,indCol)
        FilaPorConstante(Tabla,indFila,1/pivote)
        ColumnaDelPivoteCero(Tabla,indFila,indCol)
        Solucion[indFila][0] = indCol+1
        ColMultiply[indFila] = Tabla[n-1][indCol]
    for i in range(Solucion.__len__()):
        if Solucion[i][0]!=0:
            Solucion[i][1] = Tabla[i][m-1]
    print(Solucion)

# Funcion Main
if __name__ == "__main__":
    # Ejemplo para maximizar
    A = [[-1,3],[7,1]]
    B = [[6],[35]]
    z = [7,9] # Maximar esa funcion 
    print("Ejemplo para maximizar")
    Solucion = np.zeros((z.__len__(),2))
    Tabla = ConstruirTablaMaximizar(A,B,z)
    print(Tabla)
    SolMaxima = SimplexMaximizar(Tabla,Solucion)
    print(Solucion)
    # Confirmar la Solucion optima
    ProbarOptimoValor(Solucion,z,SolMaxima)  

    # Tarea 3 de la PC1
    A = [[2,1,1],[1,2,3],[2,2,1]]
    B = [[2],[5],[6]]
    z = [3,1,3] # Maximar esa funcion 
    print("\nTarea 3 PC1 para maximizar")
    Solucion = np.zeros((z.__len__(),2))
    Tabla = ConstruirTablaMaximizar(A,B,z)
    print(Tabla)
    SolMaxima = SimplexMaximizar(Tabla,Solucion)
    print(Solucion)
    # Confirmar la Solucion optima
    ProbarOptimoValor(Solucion,z,SolMaxima) 

    # Ejemplo para minimizar
    A = [[1,4],[1,2]]
    B = [[3.5],[2.5]]
    z = [3,8]
    NumeroVariables = z.__len__()
    Tabla = ConstruirTablaMinimizar(A,B,z)
    Solucion = np.zeros((z.__len__(),2))
    print("\nEjemplo para minimizar")
    print(Tabla)
    SimplexMinimizar(Tabla,Solucion,NumeroVariables)
    MinimoValor = ConseguirValorMinimo(Solucion,z) 
    print("El Minimo Valor es: ",MinimoValor)

    # La tarea 4 de la PC1
    A = [[1,2,3],[2,2,1]]
    B = [[5],[6]]
    z = [3,4,5]
    NumeroVariables = z.__len__()
    Tabla = ConstruirTablaMinimizar(A,B,z)
    Solucion = np.zeros((z.__len__(),2))
    print("\nTarea 4 de la PC1")
    print(Tabla)
    SimplexMinimizar(Tabla,Solucion,NumeroVariables)
    MinimoValor = ConseguirValorMinimo(Solucion,z) 
    print("El Minimo Valor es: ",MinimoValor)

