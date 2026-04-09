# Resultados del Análisis Sintáctico - Conjuntos LL(1)

## Explicación de los Conjuntos

* **Conjuntos de PRIMEROS (FIRST):** Indican qué símbolos terminales pueden aparecer al inicio de cualquier cadena derivada de un No Terminal específico. Si el No Terminal puede desaparecer (derivar en cadena vacía), se incluye `epsilon`.
* **Conjuntos de SIGUIENTES (FOLLOW):** Muestran qué símbolos terminales pueden aparecer inmediatamente a la derecha de un No Terminal en el proceso de derivación. El símbolo `$` representa el fin de la cadena.
* **Conjuntos de PREDICCIÓN (PREDICT):** Se calculan para cada regla de producción individual. Le indican a un analizador sintáctico predictivo qué regla exacta debe elegir cuando está evaluando un No Terminal y lee un terminal específico en la entrada.

> **Nota sobre las gramáticas evaluadas:** Al observar los resultados de predicción, se evidencian intersecciones en los conjuntos de diferentes reglas que pertenecen a un mismo No Terminal. Esto ocurre porque las gramáticas originales contienen recursividad por la izquierda, lo que indica que, estructuralmente, no son LL(1).

---

## Resultados Ejercicio 1

### Conjuntos de PRIMEROS
* PRIMEROS(C) = {'cinco', 'epsilon'}
* PRIMEROS(B) = {'cuatro', 'seis', 'epsilon'}
* PRIMEROS(D) = {'seis', 'epsilon'}
* PRIMEROS(A) = {'cinco', 'cuatro', 'seis', 'epsilon'}
* PRIMEROS(S) = {'uno', 'cinco', 'cuatro', 'seis'}

### Conjuntos de SIGUIENTES
* SIGUIENTES(C) = {'dos', 'tres', 'uno', 'seis', '$'}
* SIGUIENTES(B) = {'dos', 'tres', 'uno', 'cinco', 'seis', '$'}
* SIGUIENTES(D) = {'dos', 'tres', 'uno', 'cuatro', 'seis', '$'}
* SIGUIENTES(A) = {'tres', 'uno'}
* SIGUIENTES(S) = {'dos', '$'}

### Conjuntos de PREDICCIÓN
* PRED(S -> A uno B C) = {'uno', 'cinco', 'cuatro', 'seis'}
* PRED(S -> S dos) = {'uno', 'cinco', 'cuatro', 'seis'}
* PRED(A -> B C D) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* PRED(A -> A tres) = {'tres', 'cinco', 'cuatro', 'seis'}
* PRED(A -> epsilon) = {'tres', 'uno'}
* PRED(B -> D cuatro C tres) = {'cuatro', 'seis'}
* PRED(B -> epsilon) = {'dos', 'tres', 'uno', 'cinco', 'seis', '$'}
* PRED(C -> cinco D B) = {'cinco'}
* PRED(C -> epsilon) = {'dos', 'tres', 'uno', 'seis', '$'}
* PRED(D -> seis) = {'seis'}
* PRED(D -> epsilon) = {'dos', 'tres', 'uno', 'cuatro', 'seis', '$'}

---

## Resultados Ejercicio 2

### Conjuntos de PRIMEROS
* PRIMEROS(C) = {'cinco', 'cuatro'}
* PRIMEROS(B) = {'cinco', 'tres', 'cuatro', 'epsilon'}
* PRIMEROS(D) = {'seis', 'epsilon'}
* PRIMEROS(A) = {'dos', 'epsilon'}
* PRIMEROS(S) = {'uno', 'cinco', 'dos', 'tres', 'cuatro'}

### Conjuntos de SIGUIENTES
* SIGUIENTES(C) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* SIGUIENTES(B) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* SIGUIENTES(D) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* SIGUIENTES(A) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* SIGUIENTES(S) = {'$'}

### Conjuntos de PREDICCIÓN
* PRED(S -> A B uno) = {'uno', 'cinco', 'dos', 'tres', 'cuatro'}
* PRED(A -> dos B) = {'dos'}
* PRED(A -> epsilon) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* PRED(B -> C D) = {'cinco', 'cuatro'}
* PRED(B -> tres) = {'tres'}
* PRED(B -> epsilon) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
* PRED(C -> cuatro A B) = {'cuatro'}
* PRED(C -> cinco) = {'cinco'}
* PRED(D -> seis) = {'seis'}
* PRED(D -> epsilon) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
