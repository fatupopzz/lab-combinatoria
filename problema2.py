def criba_eratostenes(limite):
    """
    Implementa la Criba de Eratóstenes que es una aplicación
    del principio de inclusión-exclusión.
    
    Lógica:
    1. Empezamos con todos los números del 2 al límite (inclusión)
    2. Vamos excluyendo múltiplos de cada primo que encontramos
    """
    # Conjunto inicial: todos los candidatos
    candidatos = set(range(2, limite))
    primos = []
    
    # Conjuntos de múltiplos para mostrar el proceso
    multiplos_excluidos = {}
    
    while candidatos:
        # El menor número que queda es primo
        primo = min(candidatos)
        primos.append(primo)
        
        # Generamos el conjunto de múltiplos de este primo
        multiplos = set(range(primo, limite, primo))
        multiplos_excluidos[primo] = multiplos.copy()
        
        # Excluimos estos múltiplos de los candidatos
        candidatos -= multiplos
    
    return primos, multiplos_excluidos

def generar_primos_tradicional(limite):
    """
    Método tradicional para comparar
    """
    def es_primo(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for divisor in range(3, int(n ** 0.5) + 1, 2):
            if n % divisor == 0:
                return False
        return True
    
    return [n for n in range(2, limite) if es_primo(n)]

# Ejecutar el análisis
limite = 100

print("=" * 70)
print("CONTEO DE NÚMEROS PRIMOS MENORES QUE 100")
print("Usando el Principio de Inclusión-Exclusión")
print("=" * 70)

# Método 1: Usando inclusión-exclusión (Criba de Eratóstenes)
primos, multiplos_excluidos = criba_eratostenes(limite)

print("\n--- PROCESO DE INCLUSIÓN-EXCLUSIÓN ---")
print("\n1. CONJUNTO INICIAL (Inclusión):")
print(f"   Candidatos: {{2, 3, 4, 5, ..., 99}}")
print(f"   Total: {limite - 2} números")

print("\n2. CONJUNTOS DE EXCLUSIÓN (múltiplos de cada primo):")
primeros_primos = list(multiplos_excluidos.keys())[:5]
for primo in primeros_primos:
    multiplos = multiplos_excluidos[primo]
    multiplos_lista = sorted(list(multiplos))[:10]
    print(f"\n   Primo {primo}:")
    print(f"   Múltiplos a excluir: {multiplos_lista}...")
    print(f"   Total de múltiplos: {len(multiplos)}")

print("\n3. APLICANDO INCLUSIÓN-EXCLUSIÓN:")
print("   Candidatos - Múltiplos(2) - Múltiplos(3) - Múltiplos(5) - ...")

print("\n" + "=" * 70)
print("RESULTADOS FINALES")
print("=" * 70)

print(f"\nNúmeros primos menores que {limite}:")
print(primos)

print(f"\nTotal de primos encontrados: {len(primos)}")

# Mostrar algunos conjuntos usados en el cálculo
print("\n" + "-" * 70)
print("CONJUNTOS UTILIZADOS EN EL CÁLCULO:")
print("-" * 70)

print("\nConjunto de múltiplos de 2 (números pares a excluir):")
print(sorted(list(multiplos_excluidos[2]))[:20], "...")

print("\nConjunto de múltiplos de 3:")
print(sorted(list(multiplos_excluidos[3]))[:20], "...")

print("\nConjunto de múltiplos de 5:")
print(sorted(list(multiplos_excluidos[5]))[:20], "...")

print("\nConjunto de múltiplos de 7:")
print(sorted(list(multiplos_excluidos[7]))[:15], "...")

# Verificación con método tradicional
print("\n" + "=" * 70)
print("VERIFICACIÓN")
print("=" * 70)
primos_tradicional = generar_primos_tradicional(limite)
print(f"Método inclusión-exclusión: {len(primos)} primos")
print(f"Método tradicional: {len(primos_tradicional)} primos")
print(f"¿Coinciden? {'✓ SÍ' if primos == primos_tradicional else '✗ NO'}")
