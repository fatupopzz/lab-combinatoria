# Laboratorio de Análisis Combinatorio

Ejercicios de matemática discreta - Análisis combinatorio con Python

## Descripción

Este repositorio contiene la implementación de tres problemas de análisis combinatorio, 
explorando conceptos como:
- Generación y clasificación de sucesiones
- Principio de inclusión-exclusión
- Combinaciones con repetición
- Análisis de complejidad algorítmica

## Estructura del Proyecto
```
lab-combinatoria/
├── problema1.py          # Sucesiones de 4 dígitos
├── problema2.py          # Números primos (inclusión-exclusión)
├── problema3.py          # Análisis de loops anidados
└── README.md
```

## Problemas

### Problema 1: Sucesiones de 4 Dígitos

Genera y analiza todas las sucesiones decimales de 4 dígitos (0-9), donde el 0 
puede estar a la izquierda.

**Análisis realizado:**
- a) Sucesiones con 4 dígitos diferentes
- b) Sucesiones con dígitos repetidos
- c) Clasificación por patrón de repetición:
  - Un dígito 4 veces
  - Dos dígitos 2 veces cada uno
  - Un dígito 2 veces, otros únicos
  - Un dígito 3 veces, otro único

**Ejecución:**
```bash
python3 problema1.py
```

**Conceptos aplicados:**
- Generación exhaustiva
- Conjuntos y frecuencias
- Particiones de conjuntos

---

### Problema 2: Números Primos (Inclusión-Exclusión)

Cuenta todos los números primos menores que 100 usando el principio de 
inclusión-exclusión (Criba de Eratóstenes).

**Análisis realizado:**
- Generación del conjunto inicial de candidatos
- Creación de conjuntos de exclusión (múltiplos de primos)
- Aplicación del principio de inclusión-exclusión
- Listado final de números primos

**Ejecución:**
```bash
python3 problema2.py
```

**Conceptos aplicados:**
- Principio de inclusión-exclusión
- Criba de Eratóstenes
- Operaciones con conjuntos
- Teoría de números

---

### Problema 3: Análisis de Loops Anidados

Analiza un código con 5 loops anidados y demuestra su equivalencia con 
combinaciones con repetición.

**Código analizado:**
```python
for i1 in range(1,n+1):
    for i2 in range(1,i1+1):
        for i3 in range(1,i2+1):
            for i4 in range(1,i3+1):
                for i5 in range(1,i4+1):
                    k=k+1
```

**Análisis realizado:**
- Generación de tuplas (i5, i4, i3, i2, i1)
- Generación de muestras con remplazo
- Comparación de ambos conjuntos
- Verificación matemática con C(n+m-1, m)

**Ejecución:**
```bash
python3 problema3.py
```

**Conceptos aplicados:**
- Combinaciones con repetición
- Complejidad algorítmica
- Recursión
- Análisis de equivalencia

---

## Requisitos

- Python 3.x
- No requiere librerías externas

## Instalación y Uso
```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/lab-combinatoria.git
cd lab-combinatoria

# Ejecutar cualquier problema
python3 problema1.py
python3 problema2.py
python3 problema3.py
```

## Resultados Esperados

### Problema 1
- Total de sucesiones: 10,000
- Sucesiones con dígitos diferentes: 5,040
- Sucesiones con repetidos: 4,960

### Problema 2
- Números primos menores que 100: 25 primos
- Lista: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

### Problema 3
- Valor de k: 462
- Equivalente a C(11, 5) = 462
- Conclusión: El código genera todas las combinaciones con repetición

## Autor

Universidad del Valle de Guatemala - Matemática Discreta

## Licencia

Este proyecto es de código abierto para fines educativos.
