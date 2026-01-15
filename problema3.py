def simular_codigo_original(n, m):
    """
    Simula el código original y guarda todas las tuplas generadas
    """
    k = 0
    tuplas = []
    
    for i1 in range(1, n+1):
        for i2 in range(1, i1+1):
            for i3 in range(1, i2+1):
                for i4 in range(1, i3+1):
                    for i5 in range(1, i4+1):
                        k = k + 1
                        # Guardamos la tupla en el orden pedido: (i5, i4, i3, i2, i1)
                        tuplas.append((i5, i4, i3, i2, i1))
    
    return k, tuplas

def generar_muestras_con_remplazo(n_elementos, tamano_muestra):
    """
    Genera todas las muestras de 'tamano_muestra' elementos
    de un conjunto de 'n_elementos' elementos CON remplazo.
    
    Estas son combinaciones con repetición donde el ORDEN NO importa,
    por lo que las representamos en orden no decreciente.
    """
    muestras = []
    
    def generar_recursivo(muestra_actual, minimo, nivel):
        if nivel == tamano_muestra:
            muestras.append(tuple(muestra_actual))
            return
        
        for elemento in range(minimo, n_elementos + 1):
            generar_recursivo(muestra_actual + [elemento], elemento, nivel + 1)
    
    generar_recursivo([], 1, 0)
    return muestras

def combinaciones_formula(n, m):
    """
    Calcula C(n+m-1, m) usando la fórmula de combinaciones con repetición
    """
    def factorial(num):
        if num <= 1:
            return 1
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado
    
    return factorial(n + m - 1) // (factorial(m) * factorial(n - 1))

# Parámetros del problema
n = 7
m = 5

print("=" * 70)
print("ANÁLISIS DEL CÓDIGO CON LOOPS ANIDADOS")
print("=" * 70)

# Ejecutar el código original
k, tuplas_loops = simular_codigo_original(n, m)

print(f"\nValor de k después de ejecutar el código: {k}")
print(f"\nPrimeras 10 tuplas generadas (i5, i4, i3, i2, i1):")
for i, tupla in enumerate(tuplas_loops[:10]):
    print(f"  {i+1}. {tupla}")

print(f"\nÚltimas 5 tuplas generadas:")
for tupla in tuplas_loops[-5:]:
    print(f"  {tupla}")

# Generar muestras de 5 elementos de 7 con remplazo
print("\n" + "=" * 70)
print("MUESTRAS DE 5 ELEMENTOS DE 7 ELEMENTOS CON REMPLAZO")
print("=" * 70)

muestras = generar_muestras_con_remplazo(n, m)

print(f"\nTotal de muestras generadas: {len(muestras)}")
print(f"\nPrimeras 10 muestras:")
for i, muestra in enumerate(muestras[:10]):
    print(f"  {i+1}. {muestra}")

print(f"\nÚltimas 5 muestras:")
for muestra in muestras[-5:]:
    print(f"  {muestra}")

# Comparación
print("\n" + "=" * 70)
print("COMPARACIÓN DE LOS DOS CONJUNTOS")
print("=" * 70)

print(f"\nCantidad de tuplas del código: {len(tuplas_loops)}")
print(f"Cantidad de muestras con remplazo: {len(muestras)}")
print(f"¿Son iguales? {'✓ SÍ' if len(tuplas_loops) == len(muestras) else '✗ NO'}")

# Convertir a conjuntos para comparar
conjunto_tuplas = set(tuplas_loops)
conjunto_muestras = set(muestras)

print(f"\nConjunto de tuplas (tamaño): {len(conjunto_tuplas)}")
print(f"Conjunto de muestras (tamaño): {len(conjunto_muestras)}")
print(f"¿Los conjuntos son iguales? {'✓ SÍ' if conjunto_tuplas == conjunto_muestras else '✗ NO'}")

# Verificación matemática
resultado_formula = combinaciones_formula(n, m)
print(f"\nVerificación con fórmula C(n+m-1, m) = C({n}+{m}-1, {m}) = C(11, 5) = {resultado_formula}")

print("\n" + "=" * 70)
print("CONCLUSIÓN")
print("=" * 70)

