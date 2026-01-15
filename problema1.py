def generar_todas_sucesiones():
    """
    Genera todas las sucesiones de 4 dígitos (0-9)
    incluyendo las que empiezan con 0
    """
    sucesiones = []
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    sucesiones.append([d1, d2, d3, d4])
    return sucesiones

def tiene_digitos_diferentes(sucesion):
    """
    Verifica si todos los dígitos en la sucesión son diferentes
    """
    return len(set(sucesion)) == 4

def tiene_digitos_repetidos(sucesion):
    """
    Verifica si hay al menos un dígito repetido
    """
    return len(set(sucesion)) < 4

def clasificar_por_repeticion(sucesion):
    """
    Clasifica una sucesión según el patrón de repetición.
    Retorna el tipo de repetición:
    - 'cuatro_iguales': un dígito aparece 4 veces
    - 'dos_pares': dos dígitos aparecen 2 veces cada uno
    - 'un_par': un dígito aparece 2 veces, los otros son únicos
    - 'triple': un dígito aparece 3 veces, otro aparece 1 vez
    - None si todos son diferentes
    """
    conteo_digitos = {}
    for digito in sucesion:
        conteo_digitos[digito] = conteo_digitos.get(digito, 0) + 1
    
    # Ordenamos las frecuencias de mayor a menor
    frecuencias = sorted(conteo_digitos.values(), reverse=True)
    
    if frecuencias == [4]:
        return 'cuatro_iguales'
    elif frecuencias == [2, 2]:
        return 'dos_pares'
    elif frecuencias == [2, 1, 1]:
        return 'un_par'
    elif frecuencias == [3, 1]:
        return 'triple'
    else:
        return None

# Generamos todas las sucesiones posibles
todas = generar_todas_sucesiones()
print("=" * 60)
print("ANÁLISIS DE SUCESIONES DE 4 DÍGITOS")
print("=" * 60)
print(f"\nTotal de sucesiones generadas: {len(todas)}")

# Parte a) Sucesiones con dígitos diferentes
diferentes = [s for s in todas if tiene_digitos_diferentes(s)]
print("\n" + "-" * 60)
print("a) Sucesiones con 4 dígitos DIFERENTES:")
print("-" * 60)
print(f"Conteo: {len(diferentes)}")
print(f"Ejemplos: {diferentes[:5]}")

# Parte b) Sucesiones con dígitos repetidos
repetidos = [s for s in todas if tiene_digitos_repetidos(s)]
print("\n" + "-" * 60)
print("b) Sucesiones con dígitos REPETIDOS:")
print("-" * 60)
print(f"Conteo: {len(repetidos)}")
print(f"Ejemplos: {repetidos[:5]}")

# Parte c) Clasificación de las sucesiones con repetidos
print("\n" + "-" * 60)
print("c) CLASIFICACIÓN de sucesiones con repetidos:")
print("-" * 60)

clasificacion = {
    'cuatro_iguales': [],
    'dos_pares': [],
    'un_par': [],
    'triple': []
}

for sucesion in repetidos:
    tipo = clasificar_por_repeticion(sucesion)
    if tipo:
        clasificacion[tipo].append(sucesion)

print("\n1) Un dígito se repite 4 veces:")
print(f"   Conteo: {len(clasificacion['cuatro_iguales'])}")
print(f"   Ejemplos: {clasificacion['cuatro_iguales'][:3]}")

print("\n2) Dos dígitos se repiten 2 veces cada uno:")
print(f"   Conteo: {len(clasificacion['dos_pares'])}")
print(f"   Ejemplos: {clasificacion['dos_pares'][:5]}")

print("\n3) Un elemento se repite 2 veces, los otros no:")
print(f"   Conteo: {len(clasificacion['un_par'])}")
print(f"   Ejemplos: {clasificacion['un_par'][:5]}")

print("\n4) Un dígito se repite 3 veces, el otro no:")
print(f"   Conteo: {len(clasificacion['triple'])}")
print(f"   Ejemplos: {clasificacion['triple'][:5]}")

# Verificación de que la clasificación cubre todas las sucesiones
total_clasificado = sum(len(lista) for lista in clasificacion.values())
print("\n" + "=" * 60)
print("VERIFICACIÓN:")
print("=" * 60)
print(f"Total con repetidos (b): {len(repetidos)}")
print(f"Total clasificado (c):   {total_clasificado}")
print(f"¿Coinciden? {'✓ SÍ' if total_clasificado == len(repetidos) else '✗ NO'}")
print(f"\nTotal general: {len(diferentes)} + {len(repetidos)} = {len(todas)}")
